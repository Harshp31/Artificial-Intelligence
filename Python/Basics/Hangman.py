#Hangman in Python
import random

words = ("apple", "banana", "cherry", "date", "coconut")

#Dictionary of key:()
hangman_art = {0: ("       ",
                   "       ",
                   "      ",),

               1: ("   o   ",
                   "       ",
                   "       ",),

               2: ("   o.  ",
                   "   |   ",
                   "       "),

               3: ("   o   ",
                   "  /|   ",
                   "      "),

               4: ("   o   ",
                   "  /|\\  ",
                   "      "),

               5: ("   o    ",
                   "  /|\\  ",
                   "  /     "),

                6: ("   o    ",
                   "  /|\\  ",
                   "  / \\  ")}

def display_hangman(wrong_guessed):
    print("********************************")
    for line in hangman_art[wrong_guessed]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_" ] * len(answer) 
    wrong_guessed = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guessed)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guessed += 1

        
        if "_" not in hint:
            print("Congratulations! You guessed the word!")
            display_answer(answer)
            is_running = False
        elif wrong_guessed >= len(hangman_art) - 1:
            print("Game Over! You've been hanged!")
            display_answer(answer)
            is_running = False

        guessed_letters.add(guess)

if __name__ == "__main__":
        main()