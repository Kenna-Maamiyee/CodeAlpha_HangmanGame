import random

def choose_word():
    """Selects a random word from a predefined list."""
    words = [
    "apple", "tiger", "house", "plant", "river",
    "chair", "table", "phone", "light", "water",
    "music", "green", "black", "white", "stone",
    "earth", "dream", "cloud", "train", "bread",
    "smile", "laugh", "drink", "sweet", "quick"
]
    return random.choice(words)

def display_progress(word, guessed_letters):
    """Displays the current state of the guessed word."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_valid_input(guessed_letters):
    """Ensures user enters a valid single letter."""
    while True:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
        elif guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
        else:
            return guess

def hangman():
    """Main function to run the Hangman game."""
    word = choose_word()
    guessed_letters = []
    wrong_attempts = 0
    max_attempts = 6

    print("\n=== Hangman Game ===")

    while wrong_attempts < max_attempts:
        print("\nWord:", display_progress(word, guessed_letters))
        print(f"Remaining attempts: {max_attempts - wrong_attempts}")

        guess = get_valid_input(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
        else:
            wrong_attempts += 1
            print("❌ Incorrect guess.")

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break

    if wrong_attempts == max_attempts:
        print("\n💀 Game Over! The correct word was:", word)

if __name__ == "__main__":
    hangman()