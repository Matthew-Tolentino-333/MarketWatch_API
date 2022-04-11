import sys
import Bots.Strategy as Strategy

class MarketBot:
  # If no strategy passed in defaulted to SIMPLE
  def __init__(self, strategy = Strategy.Simple, watch_list = []):
    self.strategy = Strategy.StrategySelection(strategy)
    self.watch_list = watch_list

  def execute_strategy(self):
    self.strategy.execute_strategy(self.watch_list)
  
