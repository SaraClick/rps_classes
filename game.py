from random import randint


class RPS:

    _winner = None
    converter_dict = {"Rock": ["R", 0], "Paper": ["P", 1], "Scissors": ["S", 2]}

    def __init__(self, user):
        self.user = user
        self.user_move = None
        self.python_move = None
    
    def get_game_name(self):
        return "Rock, Paper, Scissor"

    def _move_converter(self, move):
        for move_name, values in self.converter_dict.items():
            if move in values:
                return move_name

    def get_and_set_user_move(self):
        u_move = input("\nEnter your move (R / S / P): ").upper()
        user_move = self._move_converter(u_move)
        self.user_move = user_move
        return user_move

    def get_and_set_python_move(self):
        p_move = randint(0, 2)
        python_move = self._move_converter(p_move)
        self.python_move = python_move
        return python_move

    def _check_winner(self):
        if self.user_move == self.python_move:
            self._winner = "None! It's a draw."
        elif (self.user_move == "Rock" and self.python_move == "Scissors") \
                or (self.user_move == "Paper" and self.python_move == "Rock") \
                or (self.user_move == "Scissors" and self.python_move == "Paper"):
            self._winner = self.user
        else:  # if none of the above if/elif is met, Python wins
            self._winner = "Python"

    def get_winner(self):
        self._check_winner()
        return self._winner

    def print_welcome_message(self):
        print("\n>>>>>> Welcome to Rock, Paper Scissors <<<<<<\n"
              "You will be playing against Python... so best of luck!\n")

    def print_rules(self):
        print("These are the moves available:")
        for key, value in self.converter_dict.items():
            print(f"{value[0]} ===> {key}")

    def print_winner(self):
        print(f"\nYour move: {self.user_move}\n"
              f"Python move: {self.python_move}\n\n"
              f">>> Winner: {self._winner} <<<")

    def play_again(self):
        again = input("\nDo you want to play again Y / N : ")
        if again.upper() == "Y" or again.upper() == "YES":
            return True
        return False





