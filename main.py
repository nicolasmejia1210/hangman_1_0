from words import choose_word
from hangman_art import HANGMAN_STAGES


def show_hidden_word(word, guessed_letters):
    """Devuelve la palabra con guiones bajos en las letras no adivinadas."""
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()


def main():
    word = choose_word()
    guessed_letters = []

    print(HANGMAN_STAGES[0])
    print("Palabra:", show_hidden_word(word, guessed_letters))

    letter = input("Ingresa una letra: ")
    print("Escribiste:", letter)


if __name__ == "__main__":
    main()