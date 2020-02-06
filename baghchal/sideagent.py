from agent import Agent
from game import Game
from const import Const
from move import Move
from typing import List
import random



class RandomAgent(Agent):
    def __init__(self,game : Game, side : int):
        super(RandomAgent, self).__init__(game,side)
    
    def propose(self) -> Move:
        if self.side == Const.MARK_GOAT:
            
            tigMoves = self.game.tigerMoves()
            tigKills : List[Move] = []
            for i in tigMoves:
                if abs(i.fromCol - i.toCol) == 2 & abs(i.fromRow - i.toRow) ==2:
                    tigKills.append(i)
            
            moves = self.game.goatMoves()
            for i in moves:
                for j in tigKills:
                    if i.toCol == j.toCol & i.toRow == j.toRow:
                        return i
            for i in moves:
                if ((i.toCol == 3 & i.toRow == 0) | \
                    (i.toCol == 0 & i.toRow == 3) | \
                    (i.toCol == 4 & i.toRow == 0) | \
                    (i.toCol == 0 & i.toRow == 4) ):
                        return i
            return random.choice(moves)
        else:
            moves = self.game.tigerMoves()
            for i in moves:
                if abs(i.fromCol - i.toCol) == 2 & abs(i.fromRow - i.toRow) ==2:
                    return i
            return random.choice(moves)
