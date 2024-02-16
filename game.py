from log import log
import os
from api.fetch_a_word import fetch_a_word
from consts import colors
from display.display_deadman import display_deadman
from display.display_score import display_score
from display.display_dashes import display_dashes

class Game:
    def __init__(self, won, lost):
        # setup a new game
        self.word = fetch_a_word()
        self.guesses = []
        self.wrong_guess = 0
        self.in_progress = True        
        self.dashed_word = ''
        self.games_won = won
        self.games_lost = lost
        self.won = False
        self.lost = False

    def display_deadman(self):
        os.system('clear')        
            
        # show a title
        log("------        Hangman v1.0       -------", colors.BLUE) 
    
        display_score(self.games_won, self.games_lost)

        # display our hangman
        display_deadman(self.wrong_guess)

        # output the dashes
        self.dashed_word = display_dashes(self.word, self.guesses)

        # set the outcome variables
        self.won = '_' not in self.dashed_word
        self.lost = self.wrong_guess >6

        if not (self.won or self.lost):
            print(f"The guesses: {self.guesses}")
            #guess
            guess = input("Make a guess:").lower()
            if guess not in self.word:
            # count the error
                self.wrong_guess += 1

            self.guesses.append(guess)
    
        