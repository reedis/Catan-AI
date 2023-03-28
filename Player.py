from Tile import resourceType
class Player:
    def __init__(self, playerNum):
        self.resources = {resourceType.BRICK: 0, resourceType.ORE: 0, resourceType.SHEEP: 0, resourceType.WHEAT: 0, resourceType.WOOD: 0}
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
            self.vp += 1
            return True
        else:
            return False
    
    def buildRoad(self):
        if self.roads != 0:
            self.roads -= 1
            return True
        else:
            return False
    
    def updateResources(self, type, count):
        print("Updating player %d" % self.playerNum)
        print(str(type))
        self.resources[type] += count
        self.totalCards += count
    
    def printPlayerStats(self):
        print("Player %d, vp: %d, settlements left: %d, roads left: %d" % (self.playerNum, self.vp, self.settlements, self.roads))

    def printPlayerResources(self):
        print("wood: %d, wheat: %d, brick: %d, ore: %d, sheep: %d," % (self.resources[resourceType.WOOD], self.resources[resourceType.WHEAT], self.resources[resourceType.BRICK], self.resources[resourceType.ORE], self.resources[resourceType.SHEEP]))
