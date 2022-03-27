from Strategy import StrategySelection

class MarketBot:
  def __init__(self, strategy):
    self.strategy = StrategySelection(strategy)

  def execute_strategy(self):
    self.strategy.execute_strategy()
  
