class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player):
        if player == "player1":
            self.score1 += 1
        else:
            self.score2 += 1

    def get_score(self):
        if self.score1 == self.score2:
            return self.score_equal(self.score1)
        if self.score1 >= 4 or self.score2 >= 4:
            return self.score_at_least_four()
        return self.mixed_score()

    def score_equal(self, score):
        if score < 3:
            equal_score = {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All"
            }.get(score)
            return equal_score
        return "Deuce"

    def score_at_least_four(self):
        difference = self.score1 - self.score2
        score = {
            1 : "Advantage player1",
            -1 : "Advantage player2",
        }.get(difference)
        if score:
            return score

        if difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def mixed_score(self):
        score_combination = {
                0 : "Love",
                1 : "Fifteen",
                2 : "Thirty",
                3 : "Forty"
            }
        score = score_combination[self.score1] + "-"
        score += score_combination[self.score2]
        return score
