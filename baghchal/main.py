from hungrytigeragent import HungryTigerAgent
from game import Game
import random
from matchup import Matchup
from hungrytigeragent import HungryTigerAgent
from stats import Stats

matchup = Matchup()
# matchup.tigerAgent = HungryTigerAgent(matchup.game)
stats = Stats(matchup, 1000)
stats.playAll()
stats.summarize()
