from log import log
from consts import colors
import os


WIN = '''!                                                (`\ .-') /`            .-') _ ,---.,---. 
!                                                 `.( OO ),'           ( OO ) )|   ||   | 
!    ,--.   ,--..-'),-----.  ,--. ,--.         ,--./  .--.  ,-.-') ,--./ ,--,' |   ||   | 
!     \  `.'  /( OO'  .-.  ' |  | |  |         |      |  |  |  |OO)|   \ |  |\ |   ||   | 
!   .-')     / /   |  | |  | |  | | .-')       |  |   |  |, |  |  \|    \|  | )|   ||   | 
!  (OO  \   /  \_) |  |\|  | |  |_|( OO )      |  |.'.|  |_)|  |(_/|  .     |/ |  .'|  .' 
!   |   /  /\_   \ |  | |  | |  | | `-' /      |         | ,|  |_.'|  |\    |  `--' `--'  
!   `-./  /.__)   `'  '-'  '('  '-'(_.-'       |   ,'.   |(_|  |   |  | \   |  .--. .--.  
!     `--'          `-----'   `-----'          '--'   '--'  `--'   `--'  `--'  '--' '--'  '''

LOSE = '''!                                                                       .-')      ('-.   
!                                                                      ( OO ).  _(  OO)  
!    ,--.   ,--..-'),-----.  ,--. ,--.          ,--.      .-'),-----. (_)---\_)(,------. 
!     \  `.'  /( OO'  .-.  ' |  | |  |          |  |.-') ( OO'  .-.  '/    _ |  |  .---' 
!   .-')     / /   |  | |  | |  | | .-')        |  | OO )/   |  | |  |\  :` `.  |  |     
!  (OO  \   /  \_) |  |\|  | |  |_|( OO )       |  |`-' |\_) |  |\|  | '..`''.)(|  '--.  
!   |   /  /\_   \ |  | |  | |  | | `-' /      (|  '---.'  \ |  | |  |.-._)   \ |  .--'  
!   `-./  /.__)   `'  '-'  '('  '-'(_.-'        |      |    `'  '-'  '\       / |  `---. 
!     `--'          `-----'   `-----'           `------'      `-----'  `-----'  `------' '''



def display_outcome(user_won, word):
    os.system('clear') 
    if user_won:
        ## you won
        log(WIN, colors.RED) 
    else:
        ## you lose
        log(LOSE, colors.RED)
        log(f"Word: {word}", colors.GREEN)