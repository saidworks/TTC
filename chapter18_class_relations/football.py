from inspect import getmembers
from pprint import pprint


# American football example
class FootballPlayer:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def displayName(self):
        print(f"Player Name :{self.name}, he plays for {self.team}")

    def isGood(self):
        print('Error! isGood is not defined')
        return False
    def printIsGood(self):
        if(self.isGood()):
            print(f"{self.name} is good")
        else:
            print(f'{self.name} is not good')


class QuarterBack(FootballPlayer):
    def __init__(self, name, team, pass_attempts, completions, pass_yards):
        super().__init__(name, team)
        self.pass_attempts = pass_attempts
        self.completions = completions
        self.pass_yards = pass_yards

    def completionRate(self):
        return round(self.completions / self.pass_attempts, 2)

    def yardsPerAttempt(self):
        return round(self.pass_yards / self.pass_attempts, 2)

    def isGood(self):
        return (self.yardsPerAttempt() > 7)


class RunningBack(FootballPlayer):
    def __init__(self, name, team, rushes, rush_yards):
        super().__init__(name, team)
        self.rushes = rushes
        self.rush_yards = rush_yards

    def yardsPerRush(self):
        return round(self.rush_yards / self.rushes, 2)

    def isGood(self):
        return (self.yardsPerRush() > 4)


player1 = QuarterBack("John", "Cowboys", 10, 6, 57)
player2 = RunningBack("Joe", 'Eagles', 12, 73)
print(player2.name)
players = []
players.extend([player1, player2])

# sidebar equivalent of var_dump in python
# pprint(getmembers(False))

player1.displayName()
print("Completion rate :", player1.completionRate(), " for ", player1.yardsPerAttempt(), "yards per attempt")
player2.displayName()
print(player2.yardsPerRush(), "yards per rush")

for player in players:
    player.displayName()
    player.printIsGood()

