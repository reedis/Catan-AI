from enum import Enum

class resourceType(Enum):
    ORE = "ORE"
    SHEEP = "SHEEP"
    WHEAT = "WHEAT"
    BRICK = "BRICK"
    WOOD = "WOOD"
    DESERT = "DESERT"

class Tile:
    def __init__(self, type, diceNumber, tileNumber):
        self.type = type
        self.diceNumber = diceNumber
        self.tileNumber = tileNumber
        self.spot1 = ("NONE", None)
        self.spot2 = ("NONE", None)
        self.spot3 = ("NONE", None)
        self.spot4 = ("NONE", None)
        self.spot5 = ("NONE", None)
        self.spot6 = ("NONE", None)
        self.road1 = ("NONE", None)
        self.road2 = ("NONE", None)
        self.road3 = ("NONE", None)
        self.road4 = ("NONE", None)
        self.road5 = ("NONE", None)
        self.road6 = ("NONE", None)

    def print(self):
        spotInfo = [0, 0, 0, 0, 0, 0]
        roadInfo = [0, 0, 0, 0, 0, 0]
        for i in range(0,6):
            spotInfo[i] = self.getSpotInfo(i+1)
            roadInfo[i] = self.getRoadInfo(i+1)
        return [str(self.tileNumber), str(self.type.value), str(self.diceNumber), spotInfo, roadInfo]

    def getSpotInfo(self, num):
        if num == 1:
            name = (", " + str( self.spot1[1])) if (not (self.spot1[1] == None)) else ''
            return (self.spot1[0] +name)
        if num == 2:
            name = (", " + str(self.spot2[1])) if (not (self.spot2[1] == None)) else ''
            return (self.spot2[0] +name)
        if num == 3:
            name = (", " + str(self.spot3[1])) if (not (self.spot3[1] == None)) else ''
            return (self.spot3[0] +name)
        if num == 4:
            name = (", " + str(self.spot4[1])) if (not (self.spot4[1] == None)) else ''
            return (self.spot4[0] +name)
        if num == 5:
            name = (", " + str(self.spot5[1])) if (not (self.spot5[1] == None)) else ''
            return (self.spot5[0] +name)
        if num == 6:
            name = (", " + str(self.spot6[1])) if (not (self.spot6[1] == None)) else ''
            return (self.spot6[0] +name)
        
    def getRoadInfo(self, num):
        if num == 1:
            name = (", " + str( self.road1[1])) if (not (self.road1[1] == None)) else ''
            return (self.road1[0] +name)
        if num == 2:
            name = (", " + str(self.road2[1])) if (not (self.road2[1] == None)) else ''
            return (self.road2[0] +name)
        if num == 3:
            name = (", " + str(self.road3[1])) if (not (self.road3[1] == None)) else ''
            return (self.road3[0] +name)
        if num == 4:
            name = (", " + str(self.road4[1])) if (not (self.road4[1] == None)) else ''
            return (self.road4[0] +name)
        if num == 5:
            name = (", " + str(self.road5[1])) if (not (self.road5[1] == None)) else ''
            return (self.road5[0] +name)
        if num == 6:
            name = (", " + str(self.road6[1])) if (not (self.road6[1] == None)) else ''
            return (self.road6[0] +name)


    def placeSettlement(self, location, player, adjList, init=False):
        def validPlace():
            if location == 1:
                return (self.spot6[1] == None) and (self.spot2[1] == None)
            elif location == 2:
                return (self.spot1[1] == None) and (self.spot3[1] == None)
            elif location == 3:
                return (self.spot2[1] == None) and (self.spot4[1] == None)
            elif location == 4:
                return (self.spot3[1] == None) and (self.spot5[1] == None)
            elif location == 5:
                return (self.spot4[1] == None) and (self.spot6[1] == None)
            elif location == 6:
                return (self.spot5[1] == None) and (self.spot1[1] == None)
            else:
                return False
            
        def roadCheck():
            if location == 1:
                return (self.road6[1] == player) or (self.road2[1] == player)
            elif location == 2:
                return (self.road1[1] == player) or (self.road3[1] == player)
            elif location == 3:
                return (self.road2[1] == player) or (self.road4[1] == player)
            elif location == 4:
                return (self.road3[1] == player) or (self.road5[1] == player)
            elif location == 5:
                return (self.road4[1] == player) or (self.road6[1] == player)
            elif location == 6:
                return (self.road5[1] == player) or (self.road1[1] == player)
            else:
                return False
        
        def neighborCheck():
            firstCheck, secondCheck = True, True
            if location == 1:
                if adjList[0]:
                    firstCheck = (adjList[0].spot2[1] == None) and (adjList[0].spot3[1] == None) and (adjList[0].spot4[1] == None)
                if adjList[1]:
                    secondCheck = (adjList[1].spot4[1] == None) and (adjList[1].spot5[1] == None) and (adjList[1].spot6[1] == None)
            elif location == 2:
                if adjList[0]:
                    firstCheck = (adjList[0].spot3[1] == None) and (adjList[0].spot4[1] == None) and (adjList[0].spot5[1] == None)
                if adjList[1]:
                    secondCheck = (adjList[1].spot5[1] == None) and (adjList[1].spot6[1] == None) and (adjList[1].spot1[1] == None)
            elif location == 3:
                if adjList[0]:
                    firstCheck = (adjList[0].spot4[1] == None) and (adjList[0].spot5[1] == None) and (adjList[0].spot6[1] == None)
                if adjList[1]:
                    secondCheck = (adjList[1].spot6[1] == None) and (adjList[1].spot1[1] == None) and (adjList[1].spot2[1] == None)
            elif location == 4:
                if adjList[0]:
                    firstCheck = (adjList[0].spot5[1] == None) and (adjList[0].spot6[1] == None) and (adjList[0].spot1[1] == None)
                if adjList[1]:
                    secondCheck = (adjList[1].spot1[1] == None) and (adjList[1].spot2[1] == None) and (adjList[1].spot3[1] == None)
            elif location == 5:
                if adjList[0]:
                    firstCheck = (adjList[0].spot6[1] == None) and (adjList[0].spot1[1] == None) and (adjList[0].spot2[1] == None)
                if adjList[1]:
                    secondCheck = (adjList[1].spot2[1] == None) and (adjList[1].spot3[1] == None) and (adjList[1].spot4[1] == None)
            elif location == 6:
                if adjList[0]:
                    firstCheck = (adjList[0].spot1[1] == None) and (adjList[0].spot2[1] == None) and (adjList[0].spot3[1] == None)
                if adjList[1]:
                    secondCheck = (adjList[1].spot3[1] == None) and (adjList[1].spot4[1] == None) and (adjList[1].spot5[1] == None)
            return firstCheck and secondCheck

        boolcheck = validPlace() if init else (validPlace() and roadCheck())
            
        if (boolcheck and neighborCheck()):
            if location == 1:
                self.spot1 = ("SETTLEMENT", player)
                if adjList[0]:
                    adjList[0].updateSettlement(3, player)
                if adjList[1]:
                    adjList[1].updateSettlement(5, player)
            elif location == 2:
                self.spot2 = ("SETTLEMENT", player)
                if adjList[0]:
                    adjList[0].updateSettlement(4, player)
                if adjList[1]:
                    adjList[1].updateSettlement(6, player)
            elif location == 3:
                self.spot3 = ("SETTLEMENT", player)
                if adjList[0]:
                    adjList[0].updateSettlement(5, player)
                if adjList[1]:
                    adjList[1].updateSettlement(1, player)
            elif location == 4:
                self.spot4 = ("SETTLEMENT", player)
                if adjList[0]:
                    adjList[0].updateSettlement(6, player)
                if adjList[1]:
                    adjList[1].updateSettlement(2, player)
            elif location == 5:
                self.spot5 = ("SETTLEMENT", player)
                if adjList[0]:
                    adjList[0].updateSettlement(1, player)
                if adjList[1]:
                    adjList[1].updateSettlement(3, player)
            elif location == 6:
                self.spot6 = ("SETTLEMENT", player)
                if adjList[0]:
                    adjList[0].updateSettlement(2, player)
                if adjList[1]:
                    adjList[1].updateSettlement(4, player)
            return True
        return False
    
    def updateSettlement(self, location, player):
        if location == 1:
            self.spot1 = ("SETTLEMENT", player)
        elif location == 2:
            self.spot2 = ("SETTLEMENT", player)
        elif location == 3:
            self.spot3 = ("SETTLEMENT", player)
        elif location == 4:
            self.spot4 = ("SETTLEMENT", player)
        elif location == 5:
            self.spot5 = ("SETTLEMENT", player)
        elif location == 6:
            self.spot6 = ("SETTLEMENT", player)
        

    def updateRoad(self, location, player):
        if location == 1:
            self.road1 = ("ROAD", player)
        elif location == 2:
            self.road2 = ("ROAD", player)
        elif location == 3:
            self.road3 = ("ROAD", player)
        elif location == 4:
            self.road4 = ("ROAD", player)
        elif location == 5:
            self.road5 = ("ROAD", player)
        elif location == 6:
            self.road6 = ("ROAD", player)

    def placeRoad(self, location, player, adj):
        def validPlace():
            if location == 1:
                return (self.road1[1] == None) and (self.spot1[1] == player) or (self.spot2[1] == player)
            elif location == 2:
                return (self.road2[1] == None) and (self.spot2[1] == player) or (self.spot3[1] == player)
            elif location == 3:
                return (self.road3[1] == None) and (self.spot3[1] == player) or (self.spot4[1] == player)
            elif location == 4:
                return (self.road4[1] == None) and (self.spot4[1] == player) or (self.spot5[1] == player)
            elif location == 5:
                return (self.road5[1] == None) and (self.spot5[1] == player) or (self.spot6[1] == player)
            elif location == 6:
                return (self.road6[1] == None) and (self.spot6[1] == player) or (self.spot1[1] == player)
            else:
                return False
            
        def neighborCheck():
            if adj:
                if location == 1:
                    return adj.spot4[1] == None
                elif location == 2:
                    return adj.spot5[1] == None
                elif location == 3:
                    return adj.spot6[1] == None
                elif location == 4:
                    return adj.spot1[1] == None
                elif location == 5:
                    return adj.spot2[1] == None
                elif location == 6:
                    return adj.spot2[1] == None
            return True
            
        if validPlace():
            if location == 1:
                self.road1 = ("ROAD", player)
                adj.updateRoad(4, player)
            elif location == 2:
                self.road2 = ("ROAD", player)
                adj.updateRoad(5, player)
            elif location == 3:
                self.road3 = ("ROAD", player)
                adj.updateRoad(6, player)
            elif location == 4:
                self.road4 = ("ROAD", player)
                adj.updateRoad(1, player)
            elif location == 5:
                self.road5 = ("ROAD", player)
                adj.updateRoad(2, player)
            elif location == 6:
                self.road6 = ("ROAD", player)
                adj.updateRoad(3, player)
            return True
        else:
            return False
            

