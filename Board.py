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
    
    def placeRoad(self, tileLoc, location, player):
        placed = False
        tile = self.getTile(tileLoc)
        adjTiles = self.getAdjTiles(tileLoc, location)
        placed = tile.placeRoad(location, player, adjTiles[1])
        return placed
    
    def getAdjTiles(self, tileNum, loc):
        tileMapping = {1: ((-1, -1), (-1, 2), (2, 5), (4, 5), (-1, 4), (-1, -1)),
                       2: ((-1, -1), (-1, 3), (6, 3), (5, 6), (1, 5), (-1, 1)), 
                       3: ((-1, -1), (-1, -1), (-1, 7), (7, 6), (6, 2), (-1, 2)), 
                       4: ((-1, 1), (1, 5), (5, 9), (9, 8), (8, -1), (-1, -1)), 
                       5: ((1, 2), (2, 6), (6, 10), (10, 9), (9, 4), (4, 1)), 
                       6: ((2, 3), (3, 7), (7, 11), (11, 10), (10, 5), (5, 2)), 
                       7: ((-1, 3), (-1, -1), (-1, 12), (12, 11), (11, 6), (6, 3)), 
                       8: ((-1, 4), (4, 9), (9, 13), (-1, 13), (-1, -1), (-1, -1)), 
                       9: ((4, 5), (5, 10), (10, 14), (14, 13), (13, 8), (8, 4)), 
                       10: ((5, 6), (6, 11), (11, 15), (15, 14), (14, 9), (9, 5)), 
                       11: ((6, 7), (7, 12), (12, 16), (16, 15), (15, 10), (10, 6)), 
                       12: ((-1, 7), (-1, -1), (-1, -1), (-1, 16), (16, 11), (11, 7)), 
                       13: ((8, 9), (9, 14), (14, 17), (-1, 17), (-1, -1), (-1, 8)), 
                       14: ((9, 10), (10, 15), (15, 18), (18, 17), (17, 13), (13, 9)), 
                       15: ((10, 11), (11, 16), (16, 19), (19, 18), (18, 14), (14, 10)), 
                       16: ((11, 12), (-1, 12), (-1, -1), (-1, 19), (19, 15), (15, 11)), 
                       17: ((13, 14), (14, 18), (-1, 18), (-1, -1), (-1, -1), (-1, 13)), 
                       18: ((14, 15), (15, 19), (-1, 19), (-1, -1), (-1, 17), (17, 14)), 
                       19: ((15, 16), (-1, 16), (-1, -1), (-1, -1), (-1, 18), (18, 15))}
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

    # Place a settlement on a temp board to find min of next turn
    def tempSettlement(self, tile, loc, player):
        ...

    def getMaxMove(self, player):
        dictVals = self.getAllSpotValues(player)
        maxMoves = []
        maxVal = max(list(dictVals.values()))
        for key,value in dictVals.items():
            if value >= maxVal:
                print(value)
                maxMoves.append(key)
        return maxMoves

    # main func to find min next move
    def getMinMove(self, nextPlayer, currentPlayer):
        tempBoard = self.board.copy()
        ...
        
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



    def getRoadOptions(tile, adj):
        ...

    