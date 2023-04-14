from Tile import resourceType
from Utils import *
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, playerNum, AI=False):
        self.resources = {resourceType.BRICK: 0, resourceType.ORE: 0, resourceType.SHEEP: 0, resourceType.WHEAT: 0, resourceType.WOOD: 0}
        self.resourceLocCount = {resourceType.BRICK: 0, resourceType.ORE: 0, resourceType.SHEEP: 0, resourceType.WHEAT: 0, resourceType.WOOD: 0}
        self.settlementLoc = []
        self.roadLoc = []
        self.totalCards = 0
        self.vp = 0
        self.settlements = 5
        self.cities = 4
        self.roads = 15
        self.devCardCount = 0
        self.devCards = {}
        self.playerNum = playerNum
        self.hasRolled = False
        self.devCardsUsed = 0
        self.isAI = AI
    
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
        
    def updateResLocCount(self, res):
        self.resourceLocCount[res] += 1
    
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
            if self.canTrade():
                moves.append(actions.TRADE)
        else:
            moves.append(actions.ROLL)

        return moves
            
    
    def updateResources(self, type, count):
        print("Updating player %d" % self.playerNum)
        print(str(type))
        self.resources[type] += count
        self.totalCards += count

    @abstractmethod
    def trade(self):
        ...

    @abstractmethod
    def playTurn(self):
        ...

    @abstractmethod
    def playSetupTurn(self):
        ...

    def tradeRes(self, oldVal, oldRes, newVal, newRes):
        self.resources[oldRes] -= oldVal
        self.resources[newRes] += newVal

    def getResFromString(self, resource):
        if resource == "BRICK":
            return resourceType.BRICK
        if resource == "ORE":
            return resourceType.ORE
        if resource == "SHEEP":
            return resourceType.SHEEP
        if resource == "WOOD":
            return resourceType.WOOD
        if resource == "WHEAT":
            return resourceType.WHEAT
        else:
            return None

    def getTradeableRes(self):
        resList = []
        for key,value in self.resources.items():
            if value >= 4:
                resList.append(key)
        return resList
    
    def displayDevCards(self):
        ...

    def useDevCards(self):
        ...
    
    def canTrade(self):
        return not len(self.getTradeableRes()) == 0
    
    def canDevCard(self):
        return not self.devCardCount == 0
    
    def addDevCard(self, res):
        if res in self.devCards:
            self.devCards[res] += 1
        else:
            self.devCards[res] = 1
        print("You have recieved one %s card" % res.value)
        return

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



class HumanPlayer(Player):
    def __init__(self, playerNum):
        super().__init__(playerNum)
    
    def trade(self):
        tradeableRes = self.getTradeableRes()
        resourcePossible = ["WOOD", "WHEAT", "ORE", "SHEEP", "BRICK"]
        resAsString = []
        print("You can trade (resource, count):")
        for item in tradeableRes:
            print("(%s, %d)" % (item.value, self.resources[item]))
            resAsString.append(item.value)
        res = "Temp"
        while (not res in resAsString):
            res = input("Please type in the resource you want to trade from the list above: ").upper().strip()
            if (not res in resAsString):
                print("Please type in a resources from the list provided")

        actualRes = self.getResFromString(res)
        count = 3
        while(not (count % 4 == 0)):
            count = int(input("Please input the resources you are trading (divisible by 4) "))
            if (not count % 4 == 0):
                print("please input a count divisible by 4")
            elif(count > self.resources[actualRes]):
                print("Please input a number inside the amount you have")
                count = 1
        newRes = "sd"
        while (not newRes in resourcePossible):
            newRes = input("What resources would you like: ").upper().strip()
            if(not newRes in resourcePossible):
                print("Please input a valid resource from below:")
                for resP in resourcePossible:
                    print(resP)
        newRes = self.getResFromString(newRes)
        newCount = count/4
        confirm = input("you want to trade %d %s for %d %s? Y/N " % (count, res, newCount, newRes.value)).lower().strip()
        if confirm == 'y':
            self.tradeRes(count, actualRes, newCount, newRes)
        else:
            print("Sorry, lets try again")
            self.trade()
    
    def playTurn(self):
        # go through a full turn, including rolling, building, and trading
        # checks to see if they want to use a dev card pre-roll
        if self.canDevCard():
            self.displayDevCards()
            devCard = input("Would you like to use one of the above dev cards? Y/N ").lower().strip()
            if devCard == 'y':
                self.useDevCards()
            elif not devCard == 'n':
                print("Invalid option, please try again")
                self.playTurn()
        #roll

        playableActions = self.getMoves()

        #build/trade
        if not len(playableActions)==0:
            ...
        else:
            input("You have no more actions you can take this round,\n press any key to end your turn")
        #end
        return 
    
    def playSetupTurn(self):
        # go through a setup turn, including building settlements and roads
        ...


class AutoPlayer(Player):
    def __init__(self, playerNum):
        super().__init__(playerNum, True)
    
    def trade(self):
        ...
    
    def playTurn(self):
        # check for pre-turn dev card
        # roll dice
        # does agent want to build? what does it want to build and where?
        # does agent want to trade? what does it want to trade?
        ...
    
    def playSetupTurn(self):
        # where does the agent want to build?
        ...