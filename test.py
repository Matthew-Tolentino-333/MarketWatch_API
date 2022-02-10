import sys

from MarketWatchAPI.util import MarketClient

def main(args):
  print('Welcome to MarktetWatch bot!')
  mc_session = MarketClient('matttolent@gmail.com', 'money4me')

  mc_session.trade('AMC', 20, 'Buy')
  # mc_session.trade('RECAF', 'OOTC', 10, Buy)
  # mc_session.trade('RECAF', 'OOTC', 10, Sell)
  # mc_session.trade('RECAF', 'OOTC', 10, Short)

  # mc_session.getSymbolData('AMC')

  print('Done testing...')

if __name__ == '__main__':
  main(sys.argv[1:])