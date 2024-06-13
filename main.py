import random
import words
import logo

chosen_word = random.choice(words.word_list)
print(logo.logo)
print(f"Passt, the solution is {chosen_word}")
health = 6
display = []
for letter in range(len(chosen_word)):
    display += "_"

end_of_game = False

while not end_of_game:
    guess_word = input("Guess the Letter:").lower()

    if guess_word in display:
        print(f"You already guessed {guess_word}")

    for i in range(0, len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess_word:
            display[i] = letter

    if guess_word not in chosen_word:
        print(f"You guessed {guess_word}, that is not in the word. U lose a health")
        health -= 1
        if health == 0:
            end_of_game = True
            print("You Lose")
    print(f"{' '.join(display)}")

    # print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win!")
    print(logo.stages[health])