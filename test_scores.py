import unittest
from scores import Scores

scores = Scores()
scores.score_board = {"testBlah": {"Hippo": 4}}
game_1 = "test1"
score1 = 13
score2 = 9
score3 = 4


class TestScores(unittest.TestCase):

    def test_check_if_max_score_empty_dict(self):
        result = scores._check_if_max_score(game_1, score1)
        expected = False
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()