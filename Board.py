from Tile import Tile
from Tile import resourceType

class Board:
    def __init__(self, randomBoard):
        tile1 = Tile(resourceType.ORE, 10, 1)
        tile2 = Tile(resourceType.SHEEP, 2, 2)
        tile3 = Tile(resourceType.WOOD, 9, 3)
        tile4 = Tile(resourceType.WHEAT, 12, 4)
        tile5 = Tile(resourceType.BRICK, 6, 5)
        tile6 = Tile(resourceType.SHEEP, 4, 6)
        tile7 = Tile(resourceType.BRICK, 10,7)
        tile8 = Tile(resourceType.WHEAT, 9, 8)
        tile9 = Tile(resourceType.WOOD, 11, 9)
        tile10 = Tile(resourceType.DESERT, 0, 10)
        tile11 = Tile(resourceType.WOOD, 3, 11)
        tile12 = Tile(resourceType.ORE, 8, 12)
        tile13 = Tile(resourceType.WOOD, 8,13)
        tile14 = Tile(resourceType.ORE, 3,14)
        tile15 = Tile(resourceType.WHEAT, 4, 15)
        tile16 = Tile(resourceType.SHEEP, 5, 16)
        tile17 = Tile(resourceType.BRICK, 5, 17)
        tile18 = Tile(resourceType.WHEAT, 6, 18)
        tile19 = Tile(resourceType.SHEEP, 10, 19)
        self.board = [[tile1, tile2, tile3], [tile4, tile5, tile6, tile7], [tile8, tile9, tile10, tile11, tile12], [tile13, tile14, tile15, tile16], [tile17, tile18, tile19]]
        self.setUp = True
        
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
        trimmedAdj = self.trimAdj(location, adjTiles)
        placed = tile.placeSettlement(location, player,  trimmedAdj, init)
        return placed
    
    def placeRoad(self, tileLoc, location, player):
        placed = False
        tile = self.getTile(tileLoc)
        adjTiles = self.getAdjTiles(tileLoc, tileLoc)
        placed = tile.placeRoad(location, player, self.trimAdj(location, adjTiles)[1])
        return placed
    
    def getAdjTiles(self, tileNum, loc):
        tileMapping = {1:(-1, 2, 5, 4, -1, -1), 2:(-1, 3, 6, 5, 1, -1), 3:(-1, -1, 7, 6, 2, -1), 
                       4:(1, 5, 9, 8, -1, -1), 5:(2, 6, 10, 9, 4, 1), 6:(3, 7, 11, 10, 5, 2), 
                       7:(-1, -1, 12, 11, 6, 3), 8:(4, 9, 13,-1,-1,-1), 9:(5, 10, 14, 13, 8, 4), 
                       10:(6, 11, 15, 14, 9, 5), 11:(7, 12, 16, 15, 10, 6), 12:(-1, -1, -1, 16, 11, 7), 
                       13:(9, 14, 17, -1, -1, 8), 14:(10, 15, 18, 17, 13, 9), 15:(11, 16, 19, 18, 14, 10), 
                       16:(12, -1, -1, 19, 15, 11), 17:(14, 18, -1, -1, -1, 13), 18:(15, 19, -1, -1, 17, 14), 
                       19:(16, -1, -1, -1, 18, 15)}
        adjList = tileMapping.get(tileNum)
        tileList = []
        for index in adjList:
            if index == -1:
                tileList.append(None)
            else:
                tileList.append(self.getTile(index))
        return tileList
    
    def trimAdj(self, loc, adjList):
        toCheck = []
        if loc == 1:
            toCheck.append(adjList[5])
            toCheck.append(adjList[0])
        elif loc == 2:
            toCheck.append(adjList[0])
            toCheck.append(adjList[1])
        elif loc == 3:
            toCheck.append(adjList[1])
            toCheck.append(adjList[2])
        elif loc == 4:
            toCheck.append(adjList[2])
            toCheck.append(adjList[3])
        elif loc == 5:
            toCheck.append(adjList[3])
            toCheck.append(adjList[4])
        elif loc == 6:
            toCheck.append(adjList[4])
            toCheck.append(adjList[5])

        return toCheck

    def getTile(self, tileNumber):
        tileCounter = 1
        for row in self.board:
            for tile in row:
                if tileCounter == tileNumber:
                    return tile
                else:
                     tileCounter += 1
    
    def getValidMoves(self, tileNumber, location, player):
        #todo
        return