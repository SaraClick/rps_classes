
class Scores:

    score_board = {}
    # key = game name  values dict with 3 max scores with key:value name:score
    # scores_board = {"RPS": {1: ["Player1", 34], 2: ["Player2", 33], 3: ["Player3", 30]}}

    def _check_if_max_score(self, game_name):
        game_record = False
        for game, top_three in self.score_board.items():
            if game == game_name:
                game_record = True
        return game_record

    def update_score_board(self, player_name, game_name, game_score):
        if not self._check_if_max_score(game_name):
            self.score_board[game_name] = {1: [player_name, game_score]}
        else:
            for game, top_three in self.score_board.items():
                if game == game_name:
                    if len(top_three) == 3:  # Case where we have 3 score records
                        if top_three[1][1] < game_score:  # score is greater than the highest score
                            top_three[3] = top_three[2]  # replace 3rd on board with current 2nd
                            top_three[2] = top_three[1]  # replace 2nd on board with current 1st
                            top_three[1] = [player_name, game_score]  # set new 1st
                        elif top_three[2][1] < game_score <= top_three[1][1]:  # if the above is not true, check if score > 2nd
                            top_three[3] = top_three[2]  # replace 3rd on board with current 2nd
                            top_three[2] = [player_name, game_score]  # set new 2nd
                        elif top_three[3][1] < game_score <= top_three[2][1]:  # if score is not > than 1st and 2nd, check if > 3rd
                            top_three[3] = [player_name, game_score]  # set new 3rd
                    elif len(top_three) == 2:
                        if top_three[1][1] < game_score:  # if score is greater than 1st
                            top_three[3] = top_three[2]
                            top_three[2] = top_three[1]
                            top_three[1] = [player_name, game_score]
                        elif top_three[2][1] < game_score <= top_three[1][1]:
                            top_three[3] = top_three[2]
                            top_three[2] = [player_name, game_score]
                        elif top_three[2][1] >= game_score:
                            top_three[3] = [player_name, game_score]  # add 3rd position to board
                    elif len(top_three) == 1:
                        if top_three[1][1] > game_score:
                            top_three[2] = [player_name, game_score]  # set new 2nd
                        else:
                            top_three[2] = top_three[1]
                            top_three[1] = [player_name, game_score]


    def get_game_played(self):
        return self.score_board.keys()

    def print_game_scores(self):
        for game, board in self.score_board.items():
            print(f">>>>   Game: {game}    <<<<")
            for name, score in board.items():
                print(f"{name} ==> {score}")










