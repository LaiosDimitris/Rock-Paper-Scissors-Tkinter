import logging
import game

logging.basicConfig(level=logging.DEBUG)

class GameTerminal:
    
    def __init__(self):
        self.rounds = None
        self.get_game_rounds()
        self.main_game()


    def get_game_rounds(self):
        while self.rounds == None:
            try:
                rounds = int(input("Enter game rounds: "))
                self.rounds = rounds
            except:
                logging.error("Incorrect round input, please try again!")


    def get_user_move(self):
        self.game.set_user_move('')
        while self.game.get_user_move() not in ['rock', 'paper', 'scissors']:
            user_move = input('Enter a move (Rock, Paper, Scissors): ')
            
            if user_move.lower() in ['rock', 'paper', 'scissors', 'r', 'p', 's']:
                if user_move == 'r':
                    self.game.set_user_move('rock')
                elif user_move == 'p':
                    self.game.set_user_move('paper')
                elif user_move == 's':
                    self.game.set_user_move('scissors')
                else:
                    self.game.set_user_move(user_move.lower())
            else:
                logging.error("Invalid move. Please enter a valid move!\n")


    def main_game(self):
        self.game = game.Game(self.rounds)
        
        for rnd in range(self.rounds):
            while True:
                logging.info(f"Round {rnd+1}\n#################")

                self.get_user_move()
                logging.info(f"User choose {self.game.get_user_move()}")

                self.game.set_computer_move()
                logging.info(f"Computer choose {self.game.get_computer_move()}")

                winner = self.game.get_round_winner()
                
                if winner == 'user':
                    logging.info(f'Round winner: User')
                    self.game.set_user_score(self.game.get_user_score() + 1)
                    break
                elif winner == 'computer':
                    logging.info(f'Round winner: Computer')
                    self.game.set_computer_score(self.game.get_computer_score() + 1)
                    break
                else:
                    logging.info(f'Draw. Replaying the round...\n')

                if winner in ['user', 'computer']:
                    if rnd+1 == self.rounds:
                        break

            logging.info(f"Score:  User: {self.game.get_user_score()} - Computer: {self.game.get_computer_score()}\n")

        winner = self.game.get_game_winner()

        if winner == 'user':
            logging.info("Game winner: User!!!")
        elif winner == 'computer':
            logging.info("Game winner: Computer!!!")
        else:
            logging.info("Draw!")
