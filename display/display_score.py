from log import log
from consts import colors


def display_score(won, lost):
    log(f"Won:{won}, lost:{lost}",colors.CYAN)
