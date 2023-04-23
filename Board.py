from Tile import *
from Utils import *
import random

class Board:
    def __init__(self, randomBoard=False):
        self.board = [[None, None, None],
                      [None,None,None,None],
                      [None,None,None,None,None],
                      [None,None,None,None],
                      [None,None,None]]
        self.tileList = [None, None, None, None, None, 
                         None, None, None, None, None,
                         None, None, None, None, None,
                         None, None, None, None]
        self.totalSpots = 54
        if randomBoard:
            self.randomBoard()
        else:
            tile1 = Tile(resourceType.ORE, 10, 1)
            tile2 = Tile(resourceType.SHEEP, 2, 2)
            tile3 = Tile(resourceType.WOOD, 9, 3)
            tile4 = Tile(resourceType.WHEAT, 12, 4)
            tile5 = Tile(resourceType.BRICK, 6, 5)
            tile6 = Tile(resourceType.SHEEP, 4, 6)
            tile7 = Tile(resourceType.BRICK, 10,7)
            tile8 = Tile(resourceType.WHEAT, 9, 8)
            tile9 = Tile(resourceType.WOOD, 11, 9)
            tile10 = Tile(resourceType.DESERT, 0, 10, True)
            tile11 = Tile(resourceType.WOOD, 3, 11)
            tile12 = Tile(resourceType.ORE, 8, 12)
            tile13 = Tile(resourceType.WOOD, 8,13)
            tile14 = Tile(resourceType.ORE, 3, 14)
            tile15 = Tile(resourceType.WHEAT, 4, 15)
            tile16 = Tile(resourceType.SHEEP, 5, 16)
            tile17 = Tile(resourceType.BRICK, 5, 17)
            tile18 = Tile(resourceType.WHEAT, 6, 18)
            tile19 = Tile(resourceType.SHEEP, 11, 19)
            self.board = [[tile1, tile2, tile3], [tile4, tile5, tile6, tile7], [tile8, tile9, tile10, tile11, tile12], [tile13, tile14, tile15, tile16], [tile17, tile18, tile19]]
            self.tileList = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, tile10, tile11, tile12, tile13, tile14, tile15, tile16, tile17, tile18, tile19]
        self.setUp = True
    
    def randomBoard(self):
        def randomRes(counts, res):
            for key, value in counts.items():
                if key == resourceType.DESERT:
                    if value > 0:
                        res.remove(key)
                        counts[key] = 0
                if key == resourceType.ORE or key == resourceType.BRICK:
                    if value >= 3:
                        res.remove(key)
                        counts[key] = 0
                elif value >=4:
                    res.remove(key)
                    counts[key] = 0
            
            retRes = random.choice(res)
            counts[retRes] += 1
            return retRes
        
        def randomNum(dice):
            randNum = random.choice(dice)
            dice.remove(randNum)
            return randNum

        countDict = {resourceType.BRICK: 0, resourceType.DESERT: 0, resourceType.ORE: 0, resourceType.SHEEP: 0, resourceType.WHEAT: 0, resourceType.WOOD: 0}

        diceProbs = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        res = [resourceType.BRICK, resourceType.WHEAT, resourceType.SHEEP, resourceType.WOOD, resourceType.ORE, resourceType.DESERT]
        tileCounter = 1
        for i in range(0,5):
            if i == 0 or i == 4:
                for j in range(0, 3):
                    randRes = randomRes(countDict, res)
                    randDice = 0
                    robber = True
                    if not randRes == resourceType.DESERT:
                        randDice = randomNum(diceProbs)
                        robber = False
                    tile = Tile(randRes, randDice, tileCounter, robber)
                    self.board[i][j] = tile
                    self.tileList[tileCounter - 1] = tile
                    tileCounter += 1
                continue
            if i == 1 or i == 3:
                for j in range(0,4):
                    randRes = randomRes(countDict, res)
                    randDice = 0
                    robber = True
                    if not randRes == resourceType.DESERT:
                        randDice = randomNum(diceProbs)
                        robber = False
                    tile = Tile(randRes, randDice, tileCounter, robber)
                    self.board[i][j] = tile
                    self.tileList[tileCounter - 1] = tile                    
                    tileCounter += 1
                continue
            else:
                for j in range(0,5):
                    randRes = randomRes(countDict, res)
                    randDice = 0
                    robber = True
                    if not randRes == resourceType.DESERT:
                        randDice = randomNum(diceProbs)
                        robber = False
                    tile = Tile(randRes, randDice, tileCounter, robber)
                    self.board[i][j] = tile
                    self.tileList[tileCounter - 1] = tile      
                    tileCounter += 1
                continue
   
    def printBoard(self, count=19):
        counter = 0
        breakFlag = False
        for row in self.board:
            for tile in row:
                print(tile.print())
                counter += 1
                if counter == count:
                    breakFlag = True
                    break
            if breakFlag:
                break

    def rolledTiles(self, roll):
        rolledTile = []
        for row in self.board:
            for tile in row:
                if tile.diceNumber == roll:
                    rolledTile.append(tile)
        return rolledTile

    def resourceMap(self):
        tileList = []
        for row in self.board:
            tileString = ''
            for tile in row:
                tileString += "|"+tile.print()[1] + ", " + tile.print()[2] + "|"
            tileList.append(tileString)
        return tileList

    def placeSettlement(self, tileLoc, location, player, init=False):
        placed = False
        tile = self.getTile(tileLoc)
        adjTiles = self.getAdjTiles(tileLoc, location)
        placed = tile.placeSettlement(location, player, adjTiles, init)
        if placed:
            self.totalSpots -= 1
        return placed
    
    def placeRoad(self, tileLoc, location, player, setUp):
        placed = False
        tile = self.getTile(tileLoc)
        adjTiles = self.getAdjTiles(tileLoc, location)
        placed = tile.placeRoad(location, player, adjTiles[1], setUp)
        return placed
    
    def getAdjTiles(self, tileNum, loc):
        adjList = tileMapping[tileNum][loc - 1]
        tileList = []
        for index in adjList:
            if index == -1:
                tileList.append(None)
            else:
                tileList.append(self.getTile(index))
        return tileList
    
    def validSettlement(self, tile, loc):
        return self.getTile(tile).validSettlementLocation(loc, self.getAdjTiles(tile, loc))

    def getTile(self, tileNumber):
        tileCounter = 1
        for row in self.board:
            for tile in row:
                if tileCounter == tileNumber:
                    return tile
                else:
                     tileCounter += 1

    def printTile(self, tileNumber):
        tile = self.getTile(tileNumber)
        num = tile.diceNumber
        res = tile.type
        ...
        
    def getSpotValue(self, tile, pos, player):
        tilesList = self.getAdjTiles(tile.tileNumber, pos)
        initTile = self.getTile(tile.tileNumber)
        tilesList.append(initTile)
        tempAdjList = tilesList.copy()
        spotVal = 0 
        for t in tilesList:
            if t:
                if not t.type == resourceType.DESERT:
                    resSpotsLeft = self.getResSpots(t.type, tempAdjList.remove(t))
                    ownedResSpots = player.resourceLocCount[t.type]
                    totalSpotsVal = self.totalSpots/(resSpotsLeft * (1 + ownedResSpots))
                    spotVal += t.getTileVal() * totalSpotsVal

        return spotVal / (4 - len(tilesList))
    
    def getResSpots(self, res, adjList):
        resTiles = self.getResTiles(res)
        totalResSpots = 0
        for tile in resTiles:
            totalResSpots += tile.openSpotCount(adjList)
        
        return totalResSpots

    def getResTiles(self, res):
        retList = []
        for tile in self.tileList:
            if tile.type == res:
                retList.append(tile)

        return retList
    
    def getAllSpotValues(self, player):
        spotDict = {}
        for t in self.tileList:
            for i in range(1,7):
                if not (t, i) in spotDict and self.validSettlement(t.tileNumber, i):
                    spotDict[(t.tileNumber,i)] = float(self.getSpotValue(t, i, player))

        return spotDict
    
    def getValidMoves(self, player, moves):
        def consecutiveRoads(roadList):
            roadDict = {}
            possibleLoc = []
            for tile, loc in roadList:
                roadDict[tile].append(loc)
            
            for key, value in roadDict:
                if len(value) >= 2:
                    possibleLoc.append((key, value))

            return possibleLoc
        
        def getOpenAdj(tileNum, loc):
            tile = self.getTile(tileNum)
            retList = []
            nextLoc = (loc + 1) % 6
            if tile.validRoadPlace(nextLoc, player.playerNum, self.getAdjTiles(tileNum, nextLoc)[1]):
                retList.append((tileNum, nextLoc))

            prevLoc = (loc - 1) % 6

            if tile.validRoadPlace(prevLoc, player.playerNum, self.getAdjTiles(tileNum, prevLoc)[1]):
                retList.append((tileNum, prevLoc))
            
            return retList

        
        def roadLocations():
            locationList = []
            roads = player.roadLoc
            settlements = player.settlementLoc

            for tile, loc in roads:
                locationList.append(getOpenAdj(tile, loc))
            return locationList
        
        for move in moves:
            if move == actions.ROAD:
                locationList = roadLocations()
                if len(locationList) == 0:
                    moves.remove(actions.ROAD)
                else:
                    moves[moves.index(actions.ROAD)] = (actions.ROAD, locationList)
            elif move == actions.SETTLEMENT:
                locationList = consecutiveRoads(player.roadLoc)
                if len(locationList) == 0:
                    moves.remove(actions.ROAD)
                else:
                    moves[moves.index(actions.ROAD)] = (actions.ROAD, locationList)
            return moves

    def getMaxMove(self, player):
        dictVals = self.getAllSpotValues(player)
        maxMoves = []
        maxVal = max(list(dictVals.values()))
        for key,value in dictVals.items():
            if value >= maxVal:
                maxMoves.append(key)
        return maxMoves

    # main func to find min next move
    def getMinMove(self, nextPlayer, currentPlayer):
        validSettlementLoc = self.getAllOpenSpots()
        moveList = []
        for spot in validSettlementLoc:
            tempBoard = self.board.copy()
            if not self.getTileMinMove(spot[0], tempBoard).type == resourceType.DESERT:
                board = self.placeSettlementMinMove(spot[0], spot[1], currentPlayer, tempBoard)
                maxMove = self.getMaxMoveMinMove(nextPlayer, board)
                moveList.append((spot, maxMove))


        minAction = None
        minVal = float("inf")
        for action, value in moveList:
            print(value[0])
            if float(value[0]) < minVal:
                print(action)
                print(value[0])
                minAction = action
                minVal = value[0]
        return minAction


    def removeAdjLoc(self, spot, listOfSpots):
        listOfSpots = listOfSpots.remove(spot)
        tn = spot[0]
        loc = spot[1]
        adjTiles = tileMapping[tn][loc]
        retList = []
        for adjSpot in listOfSpots:
            if adjSpot[0] in adjTiles:
                ...

    def distBetweenSpots(self, s1, s2, count):
        nSpots = tileMapping[s1]
        countList = []
        for v in nSpots.values():
            if v == s2:
                return count
            else:
                countList.append(self.distBetweenSpots(v, s2, count+1))
        
        return min(countList)

    def getMaxRoad(self, tileNum, loc, player):
        ## recursion depth is based on how many roads left
        recDepth = min(player.roads, 5)
        initialOptions = tileRoadMapping[(tileNum, loc)]
        return self.recRoadFinder(initialOptions, 0, recDepth, player, 0)

    def recRoadFinder(self, initMaping, acc, rec, player, depth):
        returnMap = {}
        if rec == 0:
            return acc
        

        rec -= 1
        for key, value in initMaping.items():

            acc += self.recRoadFinder(tileRoadMapping[value], acc, rec, player, depth + 1)
            if self.validSettlement(value[0], value[1]):
                acc += self.getSpotValue(self.getTile(value[0]), value[1], player)
            returnMap[value] = acc
            acc = 0
 

        maxDictVal = max(list(returnMap.values()))

        for key, value in returnMap.items():
            if value == maxDictVal:
                if depth == 0:
                    return key
                else:
                    return value
                
    def getAllOpenSpots(self):
        spotList = []
        for i in range(1, 20):
            for j in range(1, 7):
                if self.validSettlement(i, j):
                    spotList.append((i, j))

        return spotList
    
    def getSpotValueMinMove(self, tile, pos, player, board):
        tilesList = self.getAdjTilesMinMove(tile.tileNumber, pos, board)
        initTile = self.getTileMinMove(tile.tileNumber, board)
        tilesList.append(initTile)
        tempAdjList = tilesList.copy()
        spotVal = 0 
        for t in tilesList:
            if t:
                if not t.type == resourceType.DESERT:
                    resSpotsLeft = self.getResSpots(t.type, tempAdjList.remove(t))
                    ownedResSpots = player.resourceLocCount[t.type]
                    totalSpotsVal = self.totalSpots/(resSpotsLeft * (1 + ownedResSpots))
                    spotVal += t.getTileVal() * totalSpotsVal
        
        return spotVal / (4 - len(tilesList))

    def getAdjTilesMinMove(self, tileNum, loc, board):
        adjList = tileMapping[tileNum][loc - 1]
        tileList = []
        for index in adjList:
            if index == -1:
                tileList.append(None)
            else:
                tileList.append(self.getTileMinMove(index, board))
        return tileList
    
    def getTileMinMove(self, tileNumber, board):
        tileCounter = 1
        for row in board:
            for tile in row:
                if tileCounter == tileNumber:
                    return tile
                else:
                        tileCounter += 1

    def placeSettlementMinMove(self, tileLoc, location, player, board):
        tile = self.getTileMinMove(tileLoc, board)
        adjTiles = self.getAdjTilesMinMove(tileLoc, location, board)
        tile = tile.placeSettlementMin(location, player, adjTiles)
        rowInt = 0
        colInt = 0
        for row in board:
            for t in row:
                if t.getTileNumber() == tileLoc:
                    board[rowInt][colInt] = tile
                colInt += 1
            colInt = 0
            rowInt += 1
        return board
    
    def getAllSpotValuesMinMove(self, player, board):
        spotDict = {}
        copyBoard = board.copy()
        for row in copyBoard:
            for t in row:
                for i in range(1,7):
                    if not (t, i) in spotDict and self.validSettlementMinMove(t.tileNumber, i, board):
                        spotDict[(t.tileNumber, i)] = float(self.getSpotValueMinMove(t, i, player, board))
                    
        return spotDict

    def validSettlementMinMove(self, tile, loc, board):
        return self.getTileMinMove(tile, board).validSettlementLocationMin(loc, self.getAdjTilesMinMove(tile, loc, board))
    
    def getMaxMoveMinMove(self, player, board):
        dictVals = self.getAllSpotValuesMinMove(player, board)
        maxMoves = []
        maxVal = max(list(dictVals.values()))
        for key,value in dictVals.items():
            if value >= maxVal:
                maxMoves.append(value)
        return maxMoves
