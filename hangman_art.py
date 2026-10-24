# Dibujos del ahorcado en caracteres de texto.
# La posición N de la lista corresponde a N errores cometidos.
# Posición 0: sin errores. Posición 6: monigote completo (fin de la partida).

HANGMAN_STAGES = [
    # 0 errores
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    # 1 error: cabeza
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    # 2 errores: cuerpo
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    # 3 errores: brazo izquierdo
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    # 4 errores: brazo derecho
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    # 5 errores: pierna izquierda
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    # 6 errores: pierna derecha (monigote completo)
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
]