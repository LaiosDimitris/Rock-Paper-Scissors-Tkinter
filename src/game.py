import random

class Game:

    def __init__(self, rounds: int):
        # Game rounds
        self.rounds = rounds
        # User dict
        self.user = {
            "move": '',
            "score": 0
        }
        # Computer dict
        self.computer = {
            "move": '',
            "score": 0
        }

    # Setter and getter for user move
    def set_user_move(self, move: str):
        self.user['move'] = move

    def get_user_move(self):
        return self.user['move']


    # Setter and getter for user score
    def set_user_score(self, score: int):
        self.user['score'] = score

    def get_user_score(self):
        return self.user['score']


    # Setter and getter for computer move
    def set_computer_move(self):
        self.computer['move'] = random.choice(['rock', 'paper', 'scissors'])

    def get_computer_move(self):
        return self.computer['move']

    
    # Setter and getter for computer score
    def set_computer_score(self, score: int):
        self.computer['score'] = score

    def get_computer_score(self):
        return self.computer['score']

    
    # Get round winner
    def get_round_winner(self):
        # Draw
        if self.user['move'] == self.computer['move']:
            return 'draw'

        # If user has rock
        elif self.user['move'] == 'rock':
            # If computer has scissors, user wins
            if self.computer['move'] == 'scissors':
                return 'user'
            # If computer has paper, computer wins
            else:
                return 'computer'

        # If user has paper
        elif self.user['move'] == 'paper':
            # If computer has rock, user wins
            if self.computer['move'] == 'rock':
                return 'user'
            # If computer has scissors, computer wins
            else:
                return 'computer'

        # If user has scissors
        elif self.user['move'] == 'scissors':
            # If computer has paper, user wins
            if self.computer['move'] == 'paper':
                return 'user'
            # If computer has rock, computer wins
            else:
                return 'computer'


    # Get game winner
    def get_game_winner(self):
        # Draw
        if self.user['score'] == self.computer['score']:
            return 'draw'
        # User wins
        elif self.user['score'] > self.computer['score']:
            return 'user'
        # Computer wins
        else:
            return 'computer'
