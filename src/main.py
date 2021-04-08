from terminal import GameTerminal
from gui import GameGUI
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

def game_from_terminal():
    GameTerminal()

def game_from_GUI():
    GameGUI().mainloop()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        logging.error("Missing 1 argument: 'gui' or 'cmd'.")
    elif len(sys.argv) > 2:
        logging.error('Too many arguments!')
    else:
        if sys.argv[1].lower() == 'cmd':
            game_from_terminal()
        elif sys.argv[1].lower() == 'gui':
            game_from_GUI()
        else:
            logging.error("Invalid argument: Must be 'gui' or 'cmd'.")
