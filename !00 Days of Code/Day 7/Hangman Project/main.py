from random import choice
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

# Making random_word a list is better because list allows for mutability
random_word = list(choice(word_list))
number_of_lives = len(stages)
# Making the guessed word a list is better because list allows for mutability
guessed_word = list("_" * len(random_word))
guessed_letters = []

while number_of_lives != 0:
    print(stages[number_of_lives-1])
    print(f"Word = {''.join(guessed_word)}")
    letter = input("Enter the letter = ").lower()
    if letter not in guessed_letters:
        guessed_letters.append(letter)
    else:
        print("You have already guessed this particular letter.")
        continue
    # This whole if statement has code that comes into pay when the player enters a letter that is present in the
    # random word. Now what this chunk of code does is replace the "_" from the guessed word and replace them with
    # the letter itself. If there are multiple same letters present in the random word we use a while loop
    # that will remove all those letters and replace them with the "_" in the random word while doing the opposite
    # in case of the guessed word
    if letter in guessed_word:
        print("You have already guessed this particular letter.")
        continue
    if letter in random_word:
        if random_word.count(letter) > 1:
            while letter in random_word:
                i = random_word.index(letter)
                guessed_word[i] = letter
                random_word[i] = "_"
        else:
            i = random_word.index(letter)
            guessed_word[i] = letter
            random_word[i] = "_"
    # The following else statement reduces the number of the lives that the hangman has since the player has guessed
    # wrong
    else:
        number_of_lives -= 1
    # Checks whether the player has guessed all the letters correctly
    if "_" not in guessed_word:
        print("Impressive, you have guessed the word correctly!!")
        break

print("Game Over!")
