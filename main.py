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
def main():
    word = choose_word()
    guessed_letters = []

    print(HANGMAN_STAGES[0])
    print("Palabra:", show_hidden_word(word, guessed_letters))

    letter = get_letter(guessed_letters)
    guessed_letters.append(letter)
    print("Letra aceptada:", letter)


if __name__ == "__main__":
    main()