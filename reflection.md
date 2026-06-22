# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of -1 | Program should reject the input and display an "Input out of bounds" message. | Program accepts the input and displays the hint "GO HIGHER!". | None
| Restart the game after using some guesses |Clicking New Game should reset the game state and start a new game. | Game does not restart when New Game is pressed. | None |
| Change difficulty after making a guess | Changing difficulty should not affect the number of guesses already remaining. | Number of remaining guesses decreases when difficulty is changed, even though no new guess was made. | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Ans: Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). Ans: Claude suggested adding a bounds check inside parse_guess (which required passing in low and high). I verified this by testing an input of -1, and the program correctly returned an out-of-bounds error, confirming the fix worked.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). Ans: Claude generated a test file that incorrectly imported functions using import app. I verified this by running the test file, which produced import errors indicating the module structure was incorrect.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? Ans: I decided a bug was fixed when running the program with the same inputs consistently produced the expected output, especially in edge cases like invalid inputs (out-of-bounds values), and no errors were thrown.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  Ans: The test called test_parse_guess_rejects_negative with input -1 and a range of 1 to 100. It verified that the function returned ok = False, value = None, and that the error message contained "out of bounds". This confirmed that invalid inputs are correctly handled.
- Did AI help you design or understand any tests? How? Ans: Claude helped generate a test case based on my prompt about checking the bug. I used it as a starting point and reviewed it to make sure it matched the expected behavior of the function.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Ans: Streamlit "reruns" mean the entire script runs from top to bottom every time the user interacts with the app (like clicking a button or changing an input). Session state is how Streamlit remembers information between these reruns so that data or user inputs aren’t lost each time the app refreshes.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Ans: Testing habits, especially checking for possible failures and edge cases early so I can catch bugs before they become bigger problems.
- What is one thing you would do differently next time you work with AI on a coding task?
Ans: I would carefully review what the AI produces instead of assuming it is correct.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
Ans: It changed how I describe issues by focusing more on the exact error messages and expected output when asking for help with debugging.