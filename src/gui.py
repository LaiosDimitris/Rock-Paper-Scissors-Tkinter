from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image
import PIL.ImageTk
import threading
import tkinter
import logging
import time
import game

logging.basicConfig(level=logging.DEBUG)


class GameGUI(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.win_width = 700
        self.win_height = 500
        self.window_settings()
        self.load_images()
        self.initialize_ui()
        logging.info("Application ready!\n")


    def window_settings(self):
        logging.info("Configuring window setting...")
        self.title("Rock Paper Scissors")
        self.iconbitmap(r'..\data\images\gui_icon.ico')
        self.geometry(f"{self.win_width}x{self.win_height}")
        self.resizable(False, False)
    

    def load_images(self):
        # Load all the images used by the app
        logging.info("Loading images...")
        self.user_image = PIL.ImageTk.PhotoImage(Image.open(r'..\data\images\user.png').resize((183, 180), Image.ANTIALIAS))
        self.computer_image = PIL.ImageTk.PhotoImage(Image.open(r'..\data\images\computer.png').resize((183, 180), Image.ANTIALIAS))
        self.rock_image = PIL.ImageTk.PhotoImage(Image.open(r'..\data\images\rock.png').resize((54, 54), Image.ANTIALIAS))
        self.paper_image = PIL.ImageTk.PhotoImage(Image.open(r'..\data\images\paper.png').resize((54, 54), Image.ANTIALIAS))
        self.scissors_image = PIL.ImageTk.PhotoImage(Image.open(r'..\data\images\scissors.png').resize((54, 54), Image.ANTIALIAS))
        self.x_sign = PIL.ImageTk.PhotoImage(Image.open(r'..\data\images\x.png').resize((40, 40), Image.ANTIALIAS))
        self.moves_list = [self.rock_image, self.paper_image, self.scissors_image]


    def initialize_ui(self):
        logging.info("Initializing UI...")
        self.initialize_announcements_frame()
        self.initialize_main_frame()
        self.initialize_user_frame()
        self.initialize_center_frame()
        self.initialize_computer_frame()


    def initialize_announcements_frame(self):
        self.announcements_frame = tkinter.Frame(self)
        self.announcements_frame.configure(width=700, height=60, borderwidth=3, relief='sunken', bg='#ffaa42')
        self.announcements_frame.grid_propagate(False)
        self.announcements_frame.grid(row=0, column=0)

        self.announcements_label = tkinter.Label(self.announcements_frame)
        self.announcements_label.configure(width=34, font=tkFont.Font(size=25, weight='bold'), relief='flat', bg='#ffaa42', fg='white')
        self.announcements_label.grid(row=0, column=0, pady=4, padx=5)

        self.stop_game_button = tkinter.Button(self.announcements_frame)
        self.stop_game_button.configure(image=self.x_sign, bg='white', command=self.reset_game)
        # Hide until it's needed
        # self.stop_game_button.place(x=645, y=5)


    def initialize_main_frame(self):
        self.main_frame = tkinter.Frame(self)
        self.main_frame.configure(width=700, height=440, relief='ridge')
        self.main_frame.grid_propagate(False)
        self.main_frame.grid(row=1, column=0)


    def initialize_user_frame(self):
        self.user_frame = tkinter.Frame(self.main_frame)
        self.user_frame.configure(width=250, height=440, borderwidth=3, relief='ridge', bg='#ff8c00')
        self.user_frame.grid_propagate(False)
        self.user_frame.grid(row=0, column=0)

        self.user_score_label = tkinter.Label(self.user_frame)
        self.user_score_label.configure(width=2, text='0', font=tkFont.Font(family='Helvetica', size=50), borderwidth=5, relief='ridge', bg='white')
        self.user_score_label.grid(row=0, column=0, pady=10, padx=80)

        self.user_image_label = tkinter.Label(self.user_frame)
        self.user_image_label.configure(image=self.user_image, borderwidth=5, relief='ridge', bg='white')
        self.user_image_label.grid(row=1, column=0)

        self.user_name_label = tkinter.Label(self.user_frame)
        self.user_name_label.configure(width=13, text='USER', font=tkFont.Font(size=17, slant='italic', weight='bold'), borderwidth=5, relief='ridge', bg='white')
        self.user_name_label.grid(row=2, column=0)

        self.user_moves_frame = tkinter.Frame(self.user_frame)
        self.user_moves_frame.configure(borderwidth=5, relief='ridge', bg='white')
        self.user_moves_frame.grid(row=3, column=0)
        # Hide the frame until it's needed
        self.user_moves_frame.grid_remove()

        self.rock_image_button = tkinter.Button(self.user_moves_frame)
        self.rock_image_button.configure(image=self.rock_image, relief='flat', bg='white', command=lambda: self.game.set_user_move('rock'))
        self.rock_image_button.grid(row=0, column=0, padx=1)

        self.paper_image_button = tkinter.Button(self.user_moves_frame)
        self.paper_image_button.configure(image=self.paper_image, relief='flat', bg='white', command=lambda: self.game.set_user_move('paper'),)
        self.paper_image_button.grid(row=0, column=1, padx=1)

        self.scissors_image_button = tkinter.Button(self.user_moves_frame)
        self.scissors_image_button.configure(image=self.scissors_image,relief='flat', bg='white', command=lambda: self.game.set_user_move('scissors'))
        self.scissors_image_button.grid(row=0, column=2, padx=1)

        self.user_move_image = tkinter.Label(self.user_frame)
        self.user_move_image.configure(borderwidth=3, relief='ridge', bg='white')
        # Hide until it's needed
        # self.user_move_image.place(x=155, y=105)


    def initialize_center_frame(self):
        self.center_frame = tkinter.Frame(self.main_frame)
        self.center_frame.configure(width=200, height=440, borderwidth=3, relief='ridge', bg='#ffaa42')
        self.center_frame.grid_propagate(False)
        self.center_frame.grid(row=0, column=1)

        self.game_round_label = tkinter.Label(self.center_frame)
        self.game_round_label.configure(width=11, text='ROUND 1/X', font=tkFont.Font(size=20, weight='bold', slant='italic'), bg='#ff8c00', fg='white', relief='ridge', borderwidth=2)
        self.game_round_label.grid(row=0, column=0)

        self.versus_sign_label = tkinter.Label(self.center_frame)
        self.versus_sign_label.configure(text='VS', font=tkFont.Font(size=60, weight='bold'), bg='#ffaa42', fg='white')
        self.versus_sign_label.grid(row=1, column=0, padx=20, pady=100)

        self.game_round_input_frame = tkinter.Frame(self.center_frame)
        self.game_round_input_frame.configure(bg='#ffaa42')
        self.game_round_input_frame.grid(row=2, column=0)
        # Hide the frame until it's needed
        self.game_round_input_frame.grid_remove()

        self.game_round_input_label = tkinter.Label(self.game_round_input_frame)
        self.game_round_input_label.configure(width=12, text='Enter rounds:', font=tkFont.Font(size=13, weight='bold'), borderwidth=3, relief='ridge', bg='#ffaa42', fg='white')
        self.game_round_input_label.grid(row=0, column=0)

        self.game_round_input_entry = tkinter.Entry(self.game_round_input_frame)
        self.game_round_input_entry.configure(width=3, font=tkFont.Font(size=20), bg='white')
        self.game_round_input_entry.grid(row=0, column=1)

        self.start_game_button = tkinter.Button(self.center_frame)
        self.start_game_button.configure(width=12, text='START', font=tkFont.Font(size=17, weight='bold'), borderwidth=3, relief='ridge', bg='white')
        self.start_game_button.configure(command=lambda: threading.Thread(target=self.start_game, daemon=True).start())
        self.start_game_button.grid(row=3, column=0, padx=8)


    def initialize_computer_frame(self):
        self.computer_frame = tkinter.Frame(self.main_frame)
        self.computer_frame.configure(width=250, height=440, borderwidth=3, relief='ridge', bg='#ff8c00')
        self.computer_frame.grid_propagate(False)
        self.computer_frame.grid(row=0, column=2)

        self.computer_score_label = tkinter.Label(self.computer_frame)
        self.computer_score_label.configure(width=2, text='0', font=tkFont.Font(size=50), borderwidth=5, relief='ridge',bg='white')
        self.computer_score_label.grid(row=0, column=0, pady=10, padx=80)

        self.computer_image_label = tkinter.Label(self.computer_frame)
        self.computer_image_label.configure(image=self.computer_image, borderwidth=5, relief='ridge', bg='white')
        self.computer_image_label.grid(row=1, column=0)

        self.computer_name_label = tkinter.Label(self.computer_frame)
        self.computer_name_label.configure(width=13, text='COMPUTER', font=tkFont.Font(size=17, slant='italic', weight='bold'), borderwidth=5, relief='ridge', bg='white')
        self.computer_name_label.grid(row=2, column=0)

        self.computer_move_image = tkinter.Label(self.computer_frame)
        self.computer_move_image.configure(borderwidth=3, relief='ridge', bg='white')
        # Hide until it's needed
        # self.computer_move_image.place(x=300, y=105)


    def get_game_round_input(self):
        # Check if game rounds input is valid
        if self.game_round_input_entry.get() == '0':
            logging.error("User entered invalid value for round!\n")
            messagebox.showerror('Rock Paper Scissors', 'Your input is invalid!')
            return
        try:
            self.game_rounds = int(self.game_round_input_entry.get())
            self.game_round_input_entry.delete(0, 'end')
            self.game_round_input_frame.grid_remove()
        except ValueError:
            logging.error("User entered invalid value for round!\n")
            messagebox.showerror('Rock Paper Scissors', 'Your input is invalid!')
            self.game_rounds = ''


    def start_game(self):
        self.game_rounds = ''
        # Get game rounds from user
        self.game_round_input_frame.grid()
        self.start_game_button.configure(text='CONFIRM', command=lambda: self.get_game_round_input())
        self.update()

        # Wait until user enters input
        while self.game_rounds == '':
            pass

        logging.info(f"User has entered {self.game_rounds} rounds.")
        
        self.game_round_input_frame.grid_remove()
        self.start_game_button.configure(text='NEXT ROUND', command=lambda: self.get_game_round_input(self.game_round_input_entry.get()))
        # Esc button stops the game
        self.bind('<Escape>', lambda x=None: self.reset_game())
        self.update()

        self.main_game()


    def user_move(self):
        # Show available moves to user
        self.user_moves_frame.grid()
        self.announcements_label.configure(text='MAKE A MOVE')
        self.update()

        # Wait until user enters a move
        while self.game.get_user_move() == '':
            if self.game_is_running == False:
                return

        # Set the correct image
        if self.game.get_user_move() == 'rock':
            self.user_move_image.configure(image=self.rock_image)

        elif self.game.get_user_move() == 'paper':
            self.user_move_image.configure(image=self.paper_image)

        else:
            self.user_move_image.configure(image=self.scissors_image)

        # Display the user's move
        self.user_move_image.place(x=158, y=110)


    def computer_move(self):
        self.announcements_label.configure(text="COMPUTER'S MOVE")

        # Computer move animation
        for i in range(5):
            for i in range(len(self.moves_list)):
                if self.game_is_running == False:
                    return
                self.computer_move_image.configure(image=self.moves_list[i])
                self.computer_move_image.place(x=30, y=110)
                time.sleep(0.05)

        # Set a random move
        self.game.set_computer_move()

        # Set the correct image
        if self.game.get_computer_move() == 'rock':
            self.computer_move_image.configure(image=self.rock_image)

        elif self.game.get_computer_move() == 'paper':
            self.computer_move_image.configure(image=self.paper_image)

        else:
            self.computer_move_image.configure(image=self.scissors_image)

        self.update()


    def get_winner(self):
        # Get the winner of the round
        if self.game.get_round_winner() == 'user':
            self.game.set_user_score(self.game.get_user_score() + 1)
            self.user_score_label.configure(text=self.game.get_user_score())
            self.user_move_image.configure(background='green')
            self.computer_move_image.configure(background='red')
            self.announcements_label.configure(text=f"{self.game.get_round_winner().upper()} WINS!!!")

        elif self.game.get_round_winner() == 'computer':
            self.game.set_computer_score(self.game.get_computer_score() + 1)
            self.computer_score_label.configure(text=self.game.get_computer_score())
            self.computer_move_image.configure(background='green')
            self.user_move_image.configure(background='red')
            self.announcements_label.configure(text=f"{self.game.get_round_winner().upper()} WINS!!!")
        
        else:
            self.announcements_label.configure(text=f"DRAW")

        self.update()


    def next_round(self):
        # Reset the app's ui for the next round
        self.proceed_to_next_round = True
        self.start_game_button.configure(text='NEXT ROUND', state='disabled')
        self.user_move_image.place_forget()
        self.user_move_image.configure(background='white')
        self.computer_move_image.place_forget()
        self.computer_move_image.configure(background='white')
        self.game.set_user_move('')
        self.update()


    def get_game_winner(self):
        # Get the winner of the game
        if self.game.get_game_winner() == 'user':
            self.announcements_label.configure(text='USER IS THE WINNER!!!', bg='green')
        elif self.game.get_game_winner() == 'computer':
            self.announcements_label.configure(text='COMPUTER IS THE WINNER!!!', bg='red')
        else:
            self.announcements_label.configure(text='DRAW')

        self.update()


    def reset_game(self):
        # Reset the app's ui
        logging.warning("Game stopped!")
        self.game_is_running = False
        self.stop_game_button.place_forget()
        self.start_game_button.configure(text='START', state='normal')
        self.start_game_button.configure(command=lambda: threading.Thread(target=self.start_game, daemon=True).start())
        self.announcements_label.configure(text='', bg='#ffaa42')
        self.game_round_label.configure(text='ROUND 1/X')
        self.user_score_label.configure(text=0)
        self.computer_score_label.configure(text=0)
        self.user_moves_frame.grid_remove()
        self.user_move_image.place_forget()
        self.user_move_image.configure(background='white')
        self.computer_move_image.place_forget()
        self.computer_move_image.configure(background='white')
        self.unbind('<Escape>')
        self.update()


    def main_game(self):
        # Create a Game object
        logging.info("Game has started.\n")

        self.game = game.Game(self.game_rounds)

        self.game_is_running = True

        # Display stop button
        self.stop_game_button.place(x=645, y=5)

        for rnd in range(self.game.rounds):
            logging.info(f"Round {str(rnd+1)} started.\n##############################\n")
            self.game_round_label.configure(text=f'ROUND {rnd+1}/{self.game.rounds}')

            self.start_game_button.configure(text='NEXT ROUND', state='disabled' ,command=self.next_round)

            # Repeats the round if there's no winner (draw)
            while self.game.get_round_winner() not in ['user', 'computer']:
                self.user_move()

                logging.info(f"User has entered {self.game.get_user_move()}.\n")

                if self.game_is_running == False:
                    return

                self.user_moves_frame.grid_remove()
                self.update()

                self.computer_move()

                logging.info(f"Computer has entered {self.game.get_computer_move()}.\n")

                if self.game_is_running == False:
                    return

                self.get_winner()
                logging.info(f"Round winner: {self.game.get_round_winner()}.\n")

                self.start_game_button.configure(state='normal')
                if self.game.get_round_winner() == 'draw':
                    self.start_game_button.configure(text='REPLAY')
                    logging.info(f"Replaying the round...\n")
                self.update()

                if (rnd+1 == self.game.rounds) and not (self.game.get_round_winner() == 'draw'):
                    break

                self.proceed_to_next_round = False
                # Wait for user to press the button for the next round or to replay the round if it's a draw
                while not self.proceed_to_next_round:
                    if self.game_is_running == False:
                        return

            if rnd+1 == self.game.rounds:
                break

        self.start_game_button.configure(text='END', state='normal', command=self.reset_game)
        self.stop_game_button.place_forget()
        self.update()
        
        self.get_game_winner()
        logging.info(f"Game ended. Winner: {self.game.get_game_winner()}\n")
