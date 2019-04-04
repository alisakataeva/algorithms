from .data import ALPHABET_EN, BACKSPACE
from random import shuffle

def generate_text(length):

    letters = ALPHABET_EN + ALPHABET_EN.upper() + BACKSPACE*10
    text_indices = [x for x in range(length)]
    shuffle(text_indices)
    return ''.join([letters[x%len(letters)] for x in text_indices])