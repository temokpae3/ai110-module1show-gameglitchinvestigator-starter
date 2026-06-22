# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
The game’s purpose is to guess a magic number using hints that tell the player whether to go higher or lower.
- [X] Detail which bugs you found.
I found three bugs: inputs outside the valid range were not properly handled, the start button did not reset after all guesses were used, and changing the difficulty level decreased the number of remaining guesses.
- [X] Explain what fixes you applied.
I fixed the out-of-bounds issue by adding a validation check for inputs. I also fixed the reset issue by resetting st.session_state.status when restarting the game.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User sets difficulty to Normal
2. User enters a guess of -1
3. Game returns out of bounds
4. User enters a guess of 50
5. Game returns "GO LOWER"
6. User enters a guess of 40
7. Game returns "GO HIGHER"
8. User enters a guess of 35
9. Game returns "GO HIGHER"
10. User enters a guess of 37
11. Game returns "GO HIGHER"
12. User enters a guess of 38
13. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
