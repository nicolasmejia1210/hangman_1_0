import random
# las palabras en minúsculas y sin tildes ni ñ, para que coincidan con la validacion A-Z.
WORDS = [
    "python",
    "programacion",
    "computador",
    "teclado",
    "pantalla",
    "variable",
    "funcion",
    "archivo",
    "estudiante",
    "universidad",
]
def choose_word():
    """Aca se devuelve una palabra de la lista, elegida al azar."""
    return random.choice(WORDS)