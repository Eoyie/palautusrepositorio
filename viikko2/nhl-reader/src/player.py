class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nat = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.total = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20}{self.team:5}{self.goals:2} + {self.assists:2} = {self.total}"
