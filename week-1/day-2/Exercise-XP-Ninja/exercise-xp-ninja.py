my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

import sys

champion_score = 0

champion_score = 0

# --- ROUND 1 ---
print("--- ROUND 1 ---")
user_input = input("Type a long sentence (DO NOT use the letter 'A'): ")
user_input_lower = user_input.lower()

if "a" in user_input_lower:
    print("Game Over! You used the letter 'A'!")
else:
    words = user_input.split()
    champion_score = len(words)
    print(f"Safe! You are the champion with {champion_score} words!")

# --- ROUND 2 ---
print("\n--- ROUND 2 ---")
user_input = input("Can you beat the record? Type another sentence: ")
user_input_lower = user_input.lower()

if "a" in user_input_lower:
    print(f"Game Over! Record to beat remains: {champion_score}")
else:
    words = user_input.split()
    current_score = len(words)
    if current_score > champion_score:
        champion_score = current_score
        print(f"🏆 New Record! You are the champion with {champion_score} words!")
    else:
        print(f"Safe, but you didn't beat the record of {champion_score}.")

# I give up this wasnt just meant to be