class Player:
    def __init__(self, playerNum):
        self.wheat = 0
        self.ore = 0
        self.sheep = 0
        self.wood = 0
        self.brick = 0
        self.totalCards = 0
        self.vp = 0
        self.settlements = 5
        self.cities = 4
        self.roads = 15
        self.devCards = []
        self.playerNum = playerNum

    def buildSettlement(self):
        if self.settlements != 0:
            self.settlements -= 1
            return True
        else:
            return False
    
    def buildRoad(self):
        if self.roads != 0:
            self.roads -= 1
            return True
        else:
            return False