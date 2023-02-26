import unittest
from scores import Scores

scores = Scores()
game_1 = "GameName"
player1 = "P1"
player2 = "P2"
player3 = "P3"


class TestScores(unittest.TestCase):

    def test_check_if_max_score_empty_dict(self):
        result = scores._check_if_max_score(game_1)
        expected = False
        self.assertEqual(expected, result)

    def test_check_if_max_score_game_in_dict(self):
        scores.update_score_board(player1, game_1, 15)
        result = scores._check_if_max_score(game_1)
        expected = True
        self.assertEqual(expected, result)

    def test_update_score_board_2records(self):
        scores.update_score_board(player2, game_1, 9)
        result = scores.score_board[game_1]
        expected = {1: ["P1", 15], 2: ["P2", 9]}
        self.assertEqual(expected, result)

    def test_update_score_board_3records(self):
        scores.update_score_board(player2, game_1, 6)
        result = scores.score_board[game_1]
        expected = {1: ["P1", 15], 2: ["P2", 9], 3: ["P2", 6]}
        self.assertEqual(expected, result)

    def test_update_score_board_3records_add_new1st(self):
        scores.update_score_board(player3, game_1, 20)
        result = scores.score_board[game_1]
        expected = {1: ["P3", 20], 2: ["P1", 15], 3: ["P2", 9]}
        self.assertEqual(expected, result)

    def test_update_score_board_3records_add_new2nd(self):
        scores.update_score_board(player3, game_1, 17)
        result = scores.score_board[game_1]
        expected = {1: ["P3", 20], 2: ["P3", 17], 3: ["P1", 15]}
        self.assertEqual(expected, result)

    def test_update_score_board_3records_add_new3rd(self):
        scores.update_score_board(player3, game_1, 16)
        result = scores.score_board[game_1]
        expected = {1: ["P3", 20], 2: ["P3", 17], 3: ["P3", 16]}
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
