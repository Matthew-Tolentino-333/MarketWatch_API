import sys

from MarketWatchAPI.MarketWatch import MarketClient
from Bots.Strategy import *

def main(args):
  print('Welcome to MarktetWatch bot!')
  # mc_session = MarketClient('matttolent@gmail.com', 'money4me')

  # mc_session.trade('CSCO', 5, 'Buy')
  # mc_session.trade('CSCO', 2, 'Sell')
  # mc_session.trade('CSCO', 3, 'Short')

  bot1 = StrategySelection(Strat.Simple)
  bot2 = StrategySelection(Strat.DayTrade)

  print(bot1.execute_strategy())
  print(bot2.execute_strategy())
  
  print('Done testing...')

if __name__ == '__main__':
  main(sys.argv[1:])