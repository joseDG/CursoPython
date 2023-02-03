import random

from hangman_words import word_list

choose_word = random.choice(word_list)
word_length = len(choose_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

print(f'Psst, the solution is {choose_word}')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(word_length):
        letter = choose_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in choose_word:
        print(f'You guessed {guess}, that not in the word. you losse a life')

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win")

    from hangman_art import stages
    print(stages[lives])