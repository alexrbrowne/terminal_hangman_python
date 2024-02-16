from display.display_loading_screen import display_loading_screen
from display.display_outcome import display_outcome

from game import Game
from log import log
from consts import colors, status



def game_loop():
    
    display_loading_screen()
    won = 0
    lost = 0

    while(True):
        
        game = Game(won, lost)

        while(True):
                
            if game.lost:
                lost += 1
                current_game_status = status.LOST
                break
            
            if game.won:
                won += 1
                current_game_status= status.WON
                break

            game.display_deadman()
        
        # output the outcome of the game
        display_outcome(current_game_status, game.word)
        
        # play again?
        again = input("Would you like to play again? (y/n)")
        if again == 'n':
           log('Bye!', colors.RESET)
           return 

game_loop()