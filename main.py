from words import choose_word
from hangman_art import HANGMAN_STAGES

MAX_LIVES = 6


def show_hidden_word(word, guessed_letters):
    """Devuelve la palabra con guiones bajos en las letras no adivinadas."""
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()


def is_valid_input(text):
    """Comprueba que la entrada sea exactamente una letra de la A a la Z."""
    if len(text) != 1:
        return False
    return "a" <= text <= "z"


def get_letter(guessed_letters):
    """Pide una letra al jugador hasta que ingrese una entrada válida."""
    while True:
        text = input("Ingresa una letra: ").strip().lower()

        if not is_valid_input(text):
            print("Debe ingresar solo 1 letra de la A a la Z.")
            continue

        if text in guessed_letters:
            print("Ya ha utilizado la letra", text)
            continue

        return text


def play_round(word):
    """Juega una partida completa. Devuelve True si el jugador gana."""
    guessed_letters = []
    wrong_letters = []
    lives = MAX_LIVES

    while lives > 0:
        print(HANGMAN_STAGES[len(wrong_letters)])
        print("Vidas:", lives)
        print("Palabra:", show_hidden_word(word, guessed_letters))

        letter = get_letter(guessed_letters)
        guessed_letters.append(letter)

        if letter in word:
            print("¡Bien! La letra", letter, "está en la palabra.")
        else:
            wrong_letters.append(letter)
            lives -= 1
            print("No está en la palabra. Pierdes una vida.")

        if all(char in guessed_letters for char in word):
            print(HANGMAN_STAGES[len(wrong_letters)])
            print("¡Ganaste! La palabra era:", word)
            return True

    print(HANGMAN_STAGES[len(wrong_letters)])
    print("Vidas: 0")
    print("Perdiste. La palabra era:", word)
    return False


def main():
    word = choose_word()
    play_round(word)


if __name__ == "__main__":
    main()