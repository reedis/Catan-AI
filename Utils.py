from enum import Enum

class actions(Enum):
    SETTLEMENT = "SETTLEMENT"
    TRADE = "TRADE"
    ROAD = "ROAD"
    BUYDEVCARD = "BUYDEVCARD"
    USEDEVCARD = "USEDEVCARD"
    ROLL = "ROLL"

class resourceType(Enum):
    ORE = "ORE"
    SHEEP = "SHEEP"
    WHEAT = "WHEAT"
    BRICK = "BRICK"
    WOOD = "WOOD"
    DESERT = "DESERT"