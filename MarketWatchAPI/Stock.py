from bs4 import BeautifulSoup as bs
import requests

class Stock:
  def __init__(self, symbol):
    self.stock_url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

    self.getStockInformation()
   

  # Sets all stock information
  def getStockInformation(self):
    session = requests.session()
    res = session.get(self.stock_url)
    soup = bs(res.content, features='lxml')

    self.__getCurrentPrice(soup)
    self.__getGeneralInfo(soup)


  # Set current stock price
  def __getCurrentPrice(self, soup):    
    self.price = soup.find('fin-streamer', class_="Mb(-4px)").contents[0]

  def __getGeneralInfo(self, soup):
    t1 = soup.find_all(["table"])[0]
    t1_body = t1.find('tbody')
    t1_rows = t1_body.find_all('tr')
    for row_num in range(len(t1_rows)):
      ele = t1_rows[row_num].find('td', class_="Ta(end)")
    
      match row_num:
        case 0:
          self.prev_close_value = ele.contents[0]
        case 1:
          self.open_value = ele.contents[0]
        case 2:
          self.bid_value = ele.contents[0]
        case 3:
          self.ask_value = ele.contents[0]
        case 4:
          self.day_range = ele.contents[0]
        case 5:
          self.year_range = ele.contents[0]
        case 6:
          self.volume = ele.find('fin-streamer').contents[0]
        case 7:
          self.avg_volume = ele.contents[0]

    t2 = soup.find_all(["table"])[1]
    t2_body = t2.find('tbody')
    t2_rows = t2_body.find_all('tr')
    for row_num in range(len(t2_rows)):
      ele = t2_rows[row_num].find('td', class_="Ta(end)")
      
      match row_num:
        case 0:
          self.market_cap = ele.contents[0]
          break
