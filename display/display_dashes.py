from consts import colors
from log import log


def display_dashes(word:str, guesses):
    """
        display the dashes
    """
    dashes = []
    for letter in word:
        if letter == ' ':
            dashes.append(' ')
        elif letter in guesses:
          dashes.append(letter)
        else:
          dashes.append("_")
    dashed_word = " ".join(dashes)
    log(dashed_word,colors.LILAC)
    return dashed_word