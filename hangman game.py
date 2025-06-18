def play_hangman():
    

    word = "calculator"
    max_attempts = 6
    attempts = 0
    guessed_letters = set()
    display_word = ["_" for _ in word]
    incorrect_guesses = []

    while attempts < max_attempts:
        print(" ".join(display_word))
        ans = input("Guess a letter or the whole word: ").lower()

        if len(ans) == 1 and ans.isalpha():
            # Handle letter guessing as before
            if ans in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.add(ans)

            if ans in word:
                for i in range(len(word)):
                    if word[i] == ans:
                        display_word[i] = ans
                if "_" not in display_word:
                    print("Congratulations! You won!")
                    break
            else:
                attempts += 1
                incorrect_guesses.append(ans)
                print("Incorrect guess. You have guessed:", incorrect_guesses)
        elif len(ans) > 1 and ans.isalpha():
            # Handle whole word guessing
            if ans == word:
                print("Congratulations! You won!")
                break
            else:
                attempts += 1
                print("Incorrect guess.")
        else:
            print("Please enter a single letter or the whole word.")

    if "_" in display_word:
        print("Sorry, you ran out of attempts. The word was:", word)


play_hangman()