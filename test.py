import sys

from MarketWatchAPI.util import MarketClient

def main(args):
  print('Welcome to MarktetWatch bot!')
  mc_session = MarketClient()

  mc_session.order()

  print('Done testing...')

if __name__ == '__main__':
  main(sys.argv[1:])