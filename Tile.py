from Utils import resourceType



class Tile:
    def __init__(self, type, diceNumber, tileNumber, robber=False):
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
        self.spotList = [self.spot1, self.spot2, self.spot3, self.spot4, self.spot5, self.spot6]
        self.robber = robber

    def print(self):
        spotInfo = [0, 0, 0, 0, 0, 0]
        roadInfo = [0, 0, 0, 0, 0, 0]
        robber = "Robber" if self.robber else "Safe"
        for i in range(0,6):
            spotInfo[i] = self.getSpotInfo(i+1)
            roadInfo[i] = self.getRoadInfo(i+1)
        return [str(self.tileNumber), str(self.type.value), str(self.diceNumber), spotInfo, roadInfo, robber]

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

    def validSettlementLocation(self, location, adjList):
            def locCheck():
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
            
            def neighborCheck():
                firstCheck, secondCheck = True, True
                if adjList:
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
            return locCheck() and neighborCheck()

    def placeSettlement(self, location, playerClass, adjList, init=False):
        player = playerClass.playerNum

        def roadCheck():
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

        boolcheck = self.validSettlementLocation(location, adjList) 
        if init:
            boolcheck = boolcheck and roadCheck()
            
        if boolcheck:
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

            if adjList[0]:
                playerClass.updateResLocCount(adjList[0].type)
            if adjList[1]:
                playerClass.updateResLocCount(adjList[1].type)
            
            playerClass.updateResLocCount(self.type)
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
    
    def validRoadPlace(self, location, player, adj, setUp):
        def neighborCheck():
            if adj:
                if location == 1:
                    return adj.road4[1] == None
                elif location == 2:
                    return adj.road5[1] == None
                elif location == 3:
                    return adj.road6[1] == None
                elif location == 4:
                    return adj.road1[1] == None
                elif location == 5:
                    return adj.road2[1] == None
                elif location == 6:
                    return adj.road3[1] == None
            return True
        
        retBool = False
        if not setUp:
            if location == 1:
                retBool = ((self.road1[1] == None) and (self.spot1[1] == player) or 
                        (self.spot6[1] == player) or (self.road6[1] == player) or 
                        (self.road2[1] == player))
            elif location == 2:
                retBool =  ((self.road2[1] == None) and (self.spot2[1] == player) or 
                            (self.spot1[1] == player) or (self.road1[1] == player) or 
                            (self.road3[1] == player))
            elif location == 3:
                retBool =  ((self.road3[1] == None) and (self.spot3[1] == player) or 
                            (self.spot2[1] == player) or (self.road2[1] == player) or 
                            (self.road4[1] == player))
            elif location == 4:
                retBool =  ((self.road4[1] == None) and (self.spot4[1] == player) or 
                            (self.spot3[1] == player) or (self.road3[1] == player) or 
                            (self.road5[1] == player))
            elif location == 5:
                retBool =  ((self.road5[1] == None) and (self.spot5[1] == player) or 
                            (self.spot4[1] == player) or (self.road4[1] == player) or 
                            (self.road6[1] == player))
            elif location == 6:
                retBool =  ((self.road6[1] == None) and (self.spot6[1] == player) or 
                            (self.spot5[1] == player) or (self.road5[1] == player) or 
                            (self.road1[1] == player))
            else:
                retBool =  False
        else:
            retBool = True
        
        return retBool and neighborCheck()
            
    def placeRoad(self, location, play, adj, setUp):
        player = play.playerNum
        tn = self.tileNumber
        if self.validRoadPlace(location, player, adj, setUp):
            play.roadLoc.append((tn, location))
            if location == 1:
                self.road1 = ("ROAD", player)
                adj.updateRoad(4, player)
                play.roadLoc.append((adj.tileNumber, 4))
            elif location == 2:
                self.road2 = ("ROAD", player)
                adj.updateRoad(5, player)
                play.roadLoc.append((adj.tileNumber, 5))
            elif location == 3:
                self.road3 = ("ROAD", player)
                adj.updateRoad(6, player)
                play.roadLoc.append((adj.tileNumber, 6))
            elif location == 4:
                self.road4 = ("ROAD", player)
                adj.updateRoad(1, player)
                play.roadLoc.append((adj.tileNumber, 1))
            elif location == 5:
                self.road5 = ("ROAD", player)
                adj.updateRoad(2, player)
                play.roadLoc.append(2)
            elif location == 6:
                self.road6 = ("ROAD", player)
                adj.updateRoad(3, player)
                play.roadLoc.append((adj.tileNumber, 3))
            return True
        else:
            return False
        
    def getTileVal(self):
        diceProbs = {2: 1/36, 3: 1/18, 4: 1/12, 5: 1/9, 6: 5/36, 8: 5/36, 9: 1/9, 10: 1/12, 11: 1/18, 12: 1/36}
        resVals = {resourceType.BRICK: 1/6, resourceType.ORE: 2.2/3, resourceType.WHEAT: 3.2/6, resourceType.SHEEP: 1.2/5, resourceType.WOOD: 1/6}

        return (diceProbs[self.diceNumber]*resVals[self.type])
        
    def openSpotCount(self, adjList):
        spotList = []
        for i in range(1,7):
            if self.validSettlementLocation(i, adjList):
                spotList.append(i)

        return len(spotList)

    def getPayment(self, playerDict):
        if not self.robber:
            if not self.spot1[1] == None:
                playerDict[self.spot1[1]] += 1
            if not self.spot2[1] == None:
                playerDict[self.spot2[1]] += 1
            if not self.spot3[1] == None:
                playerDict[self.spot3[1]] += 1
            if not self.spot4[1] == None:
                playerDict[self.spot4[1]] += 1
            if not self.spot5[1] == None:
                playerDict[self.spot5[1]] += 1
            if not self.spot6[1] == None:
                playerDict[self.spot6[1]] += 1
        return playerDict
        
        
            

