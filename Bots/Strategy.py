import enum
from abc import ABC, abstractmethod

class Strat(enum.Enum):
  Simple = 1
  DayTrade = 2

class StrategySelection:
  def __init__(self, strategy = Strat.Simple):
    if strategy is Strat.DayTrade:
      self._strategy = DayTrade()
    else:
      self._strategy = Simple()

  def execute_strategy(self):
    return self._strategy.strategy()


class Strategy(ABC):
  @abstractmethod
  def strategy(self):
    pass


class Simple(Strategy):
  def strategy(self):
    return "This is a simple strategy"

class DayTrade(Strategy):
  def strategy(self):
    return "This is a Day Trading strategy"
