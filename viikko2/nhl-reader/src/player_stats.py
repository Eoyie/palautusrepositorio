from player import Player

class PlayerStats:
    def __init__(self, reader):

        self._reader = reader

    def top_scorers_by_nationality(self, nationality):

        response = self._reader.get_players()
        nat_players = []

        for dict_player in response:
            player = Player(dict_player)
            if player.nat == nationality:
                nat_players.append(player)

        nat_players.sort(key=lambda x: x.total, reverse=True)
        return nat_players