import sys
import time
import keyboard
from Bots.MarketBot import MarketBot

from util.MarketWatch import MarketClient
from util.Stock import Stock
from Bots.Strategy import *

bots = []
# stocks = [Stock(stock) for stock in [line.rstrip() for line in open('./Data/stocks.txt')]]

# How often to run bot strategies in seconds
sleep_time = 30

def main(args):
  quit_flag = False

  print('Welcome to MarktetWatch bot!')
  # mc_session = MarketClient('matttolent@gmail.com', 'money4me')


  stock = Stock('UONEK')
  # print(stock.price)
  # print(stock.prev_close_value)
  # print(stock.open_value)
  # print(stock.bid_value)
  # print(stock.ask_value)
  # print(stock.day_range)
  # print(stock.year_range)
  # print(stock.volume)
  # print(stock.avg_volume)
  # print(stock.market_cap)

  # mc_session.trade('CSCO', 5, 'Buy')
  # mc_session.trade('CSCO', 2, 'Sell')
  # mc_session.trade('CSCO', 3, 'Short')

  # print('foo')

  # initBots()

  # print(stocks)

  # # Execute strategies till quit
  # while True:
  #   if quit_flag:
  #     break

  #   for stock in stocks:
  #     stock.getStockInformation()

  #   for bot in bots:
  #     bot.execute_strategy()

  #   # Wait between executions and check for quit signal
  #   current_sleep = 0
  #   while current_sleep < sleep_time:
  #     if keyboard.is_pressed('q'):
  #       quit_flag = True
  #       break
  #     time.sleep(0.1)
  #     current_sleep += 0.1
  
  print('Done testing...')

def initBots():
  bots.append(MarketBot(Strat.Simple, stocks))
  bots.append(MarketBot(Strat.DayTrade, stocks))
  bots.append(MarketBot(Strat.LongShort, stocks))


if __name__ == '__main__':
  main(sys.argv[1:])