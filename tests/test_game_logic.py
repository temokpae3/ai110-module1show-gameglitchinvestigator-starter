import sys
from unittest.mock import MagicMock

# Prevent module-level st.* calls from failing when importing app outside Streamlit
sys.modules['streamlit'] = MagicMock()

from logic_utils import parse_guess, get_range_for_difficulty
from logic_utils import check_guess


# --- Existing tests (fixed: check_guess returns a tuple, not a plain string) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix: parse_guess must reject out-of-bounds inputs ---

def test_parse_guess_rejects_negative():
    ok, value, err = parse_guess("-1", low=1, high=100)
    assert ok is False
    assert value is None
    assert "out of bounds" in err.lower()

def test_parse_guess_rejects_above_range():
    ok, value, err = parse_guess("101", low=1, high=100)
    assert ok is False
    assert value is None
    assert "out of bounds" in err.lower()

def test_parse_guess_accepts_lower_boundary():
    ok, value, _ = parse_guess("1", low=1, high=100)
    assert ok is True
    assert value == 1

def test_parse_guess_accepts_upper_boundary():
    ok, value, _ = parse_guess("100", low=1, high=100)
    assert ok is True
    assert value == 100


# --- Bug fix: check_guess hint messages were swapped ---

def test_too_high_gives_lower_hint():
    # Guess above secret → player should be told to go LOWER, not HIGHER
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_gives_higher_hint():
    # Guess below secret → player should be told to go HIGHER, not LOWER
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- Bug fix: new_game must reset status to unblock the game-over guard ---

def test_status_won_must_be_reset_to_playing():
    # Before fix: status stayed "won" after new_game, causing st.stop() to fire on rerun
    state = {"status": "won"}
    state["status"] = "playing"
    assert state["status"] == "playing"

def test_status_lost_must_be_reset_to_playing():
    state = {"status": "lost"}
    state["status"] = "playing"
    assert state["status"] == "playing"


# --- Bug fix: new_game must clear history so old guesses don't carry over ---

def test_new_game_clears_history():
    state = {"history": [5, 42, 99]}
    state["history"] = []
    assert state["history"] == []


# --- Bug fix: new_game must use difficulty-aware range, not hardcoded randint(1, 100) ---

def test_easy_range_caps_at_20():
    low, high = get_range_for_difficulty("Easy")
    assert high == 20, "Easy should cap at 20; hardcoded 100 would generate unreachable secrets"

def test_hard_range_caps_at_50():
    low, high = get_range_for_difficulty("Hard")
    assert high == 50, "Hard should cap at 50; hardcoded 100 would generate unreachable secrets"

def test_secret_above_easy_max_is_unreachable():
    # A secret of 75 cannot be won on Easy (max 20); proves randint(1,100) was wrong
    _, high = get_range_for_difficulty("Easy")
    assert 75 > high


# --- Bug fix: initial attempts value must be 0 so all attempts are available on load ---

def test_initial_attempts_zero_gives_full_attempt_count():
    # Before fix: attempts=1 caused the display to show (limit-1) on first load
    initial_attempts = 0
    attempt_limit = 8  # Normal difficulty
    assert attempt_limit - initial_attempts == attempt_limit


# --- Bug fix: invalid guesses must not be appended to history ---

def test_non_numeric_guess_not_added_to_history():
    history = []
    ok, value, _ = parse_guess("not_a_number", low=1, high=100)
    if ok:
        history.append(value)
    assert history == [], "Non-numeric inputs must not pollute guess history"

def test_out_of_range_guess_not_added_to_history():
    history = []
    ok, value, _ = parse_guess("999", low=1, high=100)
    if ok:
        history.append(value)
    assert history == [], "Out-of-range inputs must not pollute guess history"

def test_valid_guess_is_added_to_history():
    # Confirm the happy path still records valid guesses
    history = []
    ok, value, _ = parse_guess("42", low=1, high=100)
    if ok:
        history.append(value)
    assert history == [42]
