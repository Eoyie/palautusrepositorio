import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsi_pelaaja_onnistuu(self):
        pelaaja = self.stats.search("Semenko")

        self.assertEqual(str(pelaaja),"Semenko EDM 4 + 12 = 16")

    def test_etsi_pelaaja_ei_ole(self):
        pelaaja = self.stats.search("Jorma")

        self.assertIsNone(pelaaja)

    def test_team_onnistuu(self):
        tiimi = self.stats.team("EDM")

        self.assertEqual(len(tiimi),3)

    def test_team_ei_onnistu(self):
        tiimi = self.stats.team("EM")

        self.assertEqual(len(tiimi),0)

    def test_top_points(self):
        top = self.stats.top(0, SortBy.POINTS)

        for i in top:
            self.assertEqual(str(i),"Gretzky EDM 35 + 89 = 124")

    def test_top_goals(self):
        top = self.stats.top(0, SortBy.GOALS)

        for i in top:
            self.assertEqual(str(i),"Lemieux PIT 45 + 54 = 99")

    def test_top_assists(self):
        top = self.stats.top(0, SortBy.ASSISTS)

        for i in top:
            self.assertEqual(str(i),"Gretzky EDM 35 + 89 = 124")
