import random

def pick_word():
    words = ["python", "java", "html", "javascript", "csharp"]
    return random.choice(words)

def display_word(word, guesses):
    display = ''
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += '-'
    return display

def get_guess(guesses):
    while True:
        guess = input("Guess a letter: ")
        if guess in guesses:
            print("You already guessed that letter. Try again.")
        else:
            return guess

word = pick_word()
guesses = []
win = []
max_attempts = 5

while True:
    print(display_word(word, guesses))
    guess = get_guess(guesses)
    guesses.append(guess)
    if guess in word:
        print("Correct!")
        win.append(guess)
    else:
        print("Incorrect.")
        max_attempts -= 1
    if max_attempts == 0:
        print("You ran out of attempts. The word was", word)
        break
    if set(word) == set(win):
        print("Congratulations! You guessed the word", word)
        break
