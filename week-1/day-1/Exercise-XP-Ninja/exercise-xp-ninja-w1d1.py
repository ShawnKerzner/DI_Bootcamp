# Exercise 4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

# Exercise 5


def sentence_without_a():
    running = True
    longest_word_count = 0
    while running:
        user_input = input("Enter a sentence without using the letter 'a': ")
        input_lowercase = user_input.lower()
        if 'a' in input_lowercase:
            print("Sentence can not contain the letter 'a'")
            choice = input("Would you like to go again? (y/n): ")
            if choice.lower() != "y":
                running = False
                print("Goodbye")
        else:
            split_input = input_lowercase.split()
            current_word_count = len(split_input)
            if current_word_count > longest_word_count:
                print(
                    f"Congratulations! Highscore: {current_word_count} Previous Highscore: {longest_word_count}")
                longest_word_count = current_word_count
                choice = input("Would you like to go again? (y/n): ")
                if choice.lower() != "y":
                    running = False
                    print("Goodbye")
            else:
                print(
                    f"Numbers of words in your sentence: {current_word_count} Highscore: {longest_word_count}")
                choice = input("Would you like to go again? (y/n): ")
                if choice.lower() != "y":
                    running = False
                    print("Goodbye")


sentence_without_a()
