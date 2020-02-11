from agent import Agent
from game import Game
from const import Const
from move import Move
from typing import List
import random



class RandomAgent(Agent):
    lastgoatcol :int = 0
    lastgoatrow :int = 0
    def __init__(self,game : Game, side : int):
        super(RandomAgent, self).__init__(game,side)
    
    def propose(self) -> Move:
        if self.side == Const.MARK_GOAT:
            
            tigMoves = self.game.tigerMoves()
            tigKills : List[Move] = []
            for i in tigMoves:
                if i.capture:
                    tigKills.append(i)
            
            moves = self.game.goatMoves()
            for i in moves:
                for j in tigKills:
                    if i.toCol == j.toCol & i.toRow == j.toRow:
                        return i
            #Take Center Edges, needs to check for potential capture
            #last Goat placement actualy makes goat wins worse
            for i in moves:
                if ((i.toCol == 0 & i.toRow == 2) | \
                    (i.toCol == 2 & i.toRow == 0) | \
                    (i.toCol == 4 & i.toRow == 2) | \
                    (i.toCol == 2 & i.toRow == 4) ):
                       # if (self.lastgoatcol != i.toCol & self.lastgoatrow != i.torow):
                        #    lastgoatcol = i.toCol
                         #   lastgoatrow = i.toRow
                     return i
            #Take corners first
            for i in moves:
                if ((i.toCol == 0 & i.toRow == 0) | \
                    (i.toCol == 0 & i.toRow == 4) | \
                    (i.toCol == 4 & i.toRow == 0) | \
                    (i.toCol == 4 & i.toRow == 4) ):
                      #  if (self.lastgoatcol != i.toCol & self.lastgoatrow != i.torow):
                       #     lastgoatcol = i.toCol
                        #    lastgoatrow = i.toRow
                       return i
            for i in moves:
                if ((i.toCol == 0) | \
                    (i.toRow == 4) | \
                    (i.toCol == 0 ) | \
                    (i.toCol == 4) ):
                      #  if (self.lastgoatcol != i.toCol & self.lastgoatrow != i.torow):
                       #     lastgoatcol = i.toCol
                        #    lastgoatrow = i.toRow
                       return i

            #Defaults to Random
            lastgoatcol = -1
            lastgoatrow = -1
            return random.choice(moves)
        else:
            moves = self.game.tigerMoves()
            #Lazy Hungry Tiger
            for i in moves:
                if i.capture:
                    return i
            return random.choice(moves)
