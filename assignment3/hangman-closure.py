# hangman-closure.py

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        result = ""

        for ch in secret_word:
            if ch.lower() in guesses:
                result += ch
            else:
                result += "_"

        print(result)

        # Check if all letters guessed
        return all(ch.lower() in guesses for ch in secret_word)

    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter the secret word: ")
    game = make_hangman(secret)

    won = False
    while not won:
        guess = input("Guess a letter: ").lower()
        won = game(guess)

    print(f"Congratulations! You guessed the word '{secret}'")
