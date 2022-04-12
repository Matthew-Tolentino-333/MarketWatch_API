import enum
from abc import ABC, abstractmethod

class Strat(enum.Enum):
  Simple = 1
  DayTrade = 2
  LongShort = 3

class StrategySelection:
  def __init__(self, strategy = Strat.Simple):
    if strategy is Strat.DayTrade:
      self._strategy = DayTrade()
    elif strategy is Strat.LongShort:
      self._strategy = LongShort()
    else:
      self._strategy = Simple()

  def execute_strategy(self, watch_list):
    return self._strategy.strategy(watch_list)


class Strategy(ABC):
  @abstractmethod
  def strategy(self, watch_list):
    print(watch_list)
    pass

class Simple(Strategy):
  def strategy(self, watch_list):
    print("This is a simple strategy")
    return

class DayTrade(Strategy):
  def strategy(self, watch_list):
    print("This is a Day Trading strategy")
    # print(watch_list)
    return

class LongShort(Strategy):
  def strategy(self, watch_list):
    print("This is a Long Short strategy")
    # print(watch_list)
    return
