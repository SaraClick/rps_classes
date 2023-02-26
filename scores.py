
class Scores:

    score_board = {}  # key = game name  values dict with 3 max scores with key:value name:score

    def _check_if_max_score(self, game_name, game_score):
        for game, top_three in self.score_board.items():
            if game == game_name:
                if game_score > top_three[2][1]:  # accessing the lowest score of the top 3 dict
                    return True
        return False

    def update_score_board(self, player_name, game_name, game_score):
        if not self._check_if_max_score(game_name, game_score):
            self.score_board[game_name] = {player_name: game_score}
        else:
            for game, top_three in self.score_board.items():
                if game == game_name:
                    if top_three[0][1] < game_score:
                        top_three[2] = top_three[1]  # replace 3rd on board with current 2nd
                        top_three[1] = top_three[0]  # replace 2nd on board with current 1st
                        top_three[0] = {player_name: game_score}  # set new 1st
                    elif top_three[0][1] < game_score:
                        top_three[2] = top_three[1] # replace 3rd on board with current 2nd
                        top_three[1] = {player_name: game_score} # set new 2nd
                    else:
                        top_three[2] = {player_name: game_score}  # set new 3rd

    def get_game_played(self):
        return self.score_board.keys()

    def print_game_scores(self):
        for game, board in self.score_board.items():
            print(f">>>>   Game: {game}    <<<<")
            for name, score in board.items():
                print(f"{name} ==> {score}")










