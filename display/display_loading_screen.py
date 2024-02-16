import os
from log import log
import sys
import time
from consts import colors

logo = '''888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               '''


def display_loading_screen():
    os.system('clear') 
    log(logo, colors.RED)
    
    for i in range(30):
        sys.stdout.write("\r[%-30s] %d%%" % ('='*i, i/30*100))
        sys.stdout.flush()
        time.sleep(0.1)
        
    sys.stdout.write("\n")