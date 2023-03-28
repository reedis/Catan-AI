from Tile import resourceType
from Utils import *

class Player:
    def __init__(self, playerNum):
        self.resources = {resourceType.BRICK: 0, resourceType.ORE: 0, resourceType.SHEEP: 0, resourceType.WHEAT: 0, resourceType.WOOD: 0}
        self.settlementLoc = []
        self.roadLoc = []
        self.totalCards = 0
        self.vp = 0
        self.settlements = 5
        self.cities = 4
        self.roads = 15
        self.devCards = []
        self.playerNum = playerNum
        self.hasRolled = False
        self.devCardsUsed = 0
    
    def endTurn(self):
        self.hasRolled = False
        self.devCardsUsed = 0

    def buildSettlement(self, tile, loc):
        if self.settlements != 0 and self.settlementRes():
            self.settlements -= 1
            self.vp += 1
            self.removeWood()
            self.removeBrick()
            self.removeWheat()
            self.removeSheep()
            return True
        else:
            return False
    
    def buildRoad(self, tile, loc):
        if self.roads != 0 and self.roadRes():
            self.removeBrick()
            self.removeWood()
            self.roads -= 1
            print(self.roadLoc)
            return True
        else:
            return False
        
    def settlementRes(self):
        return (self.roadRes() and (self.resources[resourceType.WHEAT] >= 1) and (self.resources[resourceType.SHEEP] >=1))
    
    def roadRes(self):
        return (self.resources[resourceType.BRICK] >= 1) and (self.resources[resourceType.WOOD] >= 1) 
    
    def getMoves(self):
        moves = []
        brick = self.resources[resourceType.BRICK]
        ore = self.resources[resourceType.ORE]
        wheat = self.resources[resourceType.WHEAT]
        wood = self.resources[resourceType.WOOD]
        sheep = self.resources[resourceType.SHEEP]

        ##checks for dev cards
        if len(self.devCards) > 0:
            moves.append(actions.USEDEVCARD)

        ## can only build after rolling
        if self.hasRolled:
            ##checks for resources for settlement
            if (brick and sheep and wheat and wood):
                moves.append(actions.SETTLEMENT)
            ##checks for resources for road
            if brick and wood:
                moves.append(actions.ROAD)
            ##checks for resources for dev card
            if sheep and ore and wheat:
                moves.append(actions.BUYDEVCARD)
        else:
            moves.append(actions.ROLL)

        return moves
            
    
    def updateResources(self, type, count):
        print("Updating player %d" % self.playerNum)
        print(str(type))
        self.resources[type] += count
        self.totalCards += count

    def removeWheat(self):
        self.resources[resourceType.WHEAT] -= 1 if (self.resources[resourceType.WHEAT] >=1) else 0
    
    def removeWood(self):
        self.resources[resourceType.WOOD] -= 1 if (self.resources[resourceType.WOOD] >=1) else 0
    
    def removeSheep(self):
        self.resources[resourceType.SHEEP] -= 1 if (self.resources[resourceType.SHEEP] >=1) else 0
    
    def removeOre(self):
        self.resources[resourceType.ORE] -= 1 if (self.resources[resourceType.ORE] >=1) else 0

    def removeBrick(self):
        self.resources[resourceType.BRICK] -= 1 if (self.resources[resourceType.BRICK] >=1) else 0
    
    def printPlayerStats(self):
        print("Player %d, vp: %d, settlements left: %d, roads left: %d" % (self.playerNum, self.vp, self.settlements, self.roads))

    def printPlayerResources(self):
        print("wood: %d, wheat: %d, brick: %d, ore: %d, sheep: %d," % (self.resources[resourceType.WOOD], self.resources[resourceType.WHEAT], self.resources[resourceType.BRICK], self.resources[resourceType.ORE], self.resources[resourceType.SHEEP]))
