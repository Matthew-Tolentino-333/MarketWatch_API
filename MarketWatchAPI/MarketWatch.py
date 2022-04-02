import requests
import re
import time
import random
from bs4 import BeautifulSoup

class MarketClient:
  def __init__(self, username, password, game):
    self.session = self.login(username, password)
    self.game = game
    self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
  
  def login(self, email, password):
    s = requests.Session()
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
    payload = {
      "client_id": "5hssEAdMy0mJTICnJNvC9TXEw3Va7jfO",
      "connection": "DJldap",
      "headers": {
        "X-REMOTE-USER": email
      },
      "nonce": "86614735-ebb3-4fc2-9674-d0bf0bf7fdc2",
      "ns": "prod/accounts-mw",
      "password": password,
      "protocol": "oauth2",
      "redirect_uri": "https://accounts.marketwatch.com/auth/sso/login",
      "response_type": "code",
      "scope": "openid idp_id roles email given_name family_name djid djUsername djStatus trackid tags prts suuid createTimestamp",
      "state": "hKFo2SBSS2c4UmprX3h0UDdZVEdvbVZldmJTdkhsaERkekxfSqFupWxvZ2luo3RpZNkgWjkyV0JFSHZvb1RhZ0VEbGYxb2Zla09TVk05WFRGVEijY2lk2SA1aHNzRUFkTXkwbUpUSUNuSk52QzlUWEV3M1ZhN2pmTw",
      "tenant": "sso",
      "ui_locales": "en-us-x-mw-3-8",
      "username": email,
      "_csrf": "sMAl0bPM-NtbjmegNoXqBRiNIQDvAYIWSEZc",
      "_intstate": "deprecated"
    }

    # Get state and csrf codes for login session
    res = s.get('https://accounts.marketwatch.com/login?target=https%3A%2F%2Fwww.marketwatch.com%2F')
    csrf = re.search("\=(\S*)", str(res.cookies)).group(1)
    state = re.search("(?<=\=)(.*?)(?=\&)", str(res.url)).group(1)

    payload['_csrf'] = csrf
    payload['state'] = state

    # Attempt login
    try: 
      print('Try login')

      response = s.post('https://sso.accounts.dowjones.com/usernamepassword/login', headers=headers, json=payload)
      hidden_form = BeautifulSoup(response.content, features='lxml')
      parsed_hidden_form = hidden_form.find_all('input', attrs={'type': 'hidden'})
      hidden_form_data = {}
      for input in parsed_hidden_form:
        hidden_form_data[input['name']] = input['value']
      s.post('https://sso.accounts.dowjones.com/login/callback', data=hidden_form_data, headers=headers)

      time.sleep(random.uniform(2,4))
      
      res = s.get('https://customercenter.marketwatch.com/home', headers=headers)
      if res.url == 'https://customercenter.marketwatch.com/home':
        print('Login Succesful.')
      else:
        print('Login Failure.')

    except BaseException as e:
      print('Problem with Login')
      print('Error: {}'.format(e))
      exit(1)

    # s.headers.update({'authorization': json.loads(r.content)['token']})
    return s

  def trade(self, symbol, amount, tradeType):
    print('--> {}ing...'.format(tradeType), symbol)

    symbol_data = self.getSymbolData(symbol)

    payload = {
      'djid': symbol_data['djid'],
      'expiresEndOfDay': 'false',
      'ledgerId': symbol_data['ledgerId'],
      'orderType': "Market",
      'shares': amount,
      'tradeType': tradeType
    }

    res = self.session.post('https://vse-api.marketwatch.com/v1/games/{}/ledgers/{}/trades'.format(self.game, symbol_data['ledgerId']), headers=self.headers, json=payload)
    if res.status_code == 200:
      print('{} {} of {}'.format(tradeType, amount, symbol))
    else:
      print('{} of {} failed'.format(tradeType, symbol))

  # Provide symbol and market identifier code
  def getSymbolData(self, symbol):
    charting_symbol_content = self.session.get('https://services.dowjones.com/autocomplete/data?excludeExs=xmstar&featureClass=P&style=full&count=5&need=symbol&q={}&name_startsWith={}'.format(symbol, symbol), headers=self.headers).content
    charting_symbol = re.search('STOCK\/US\/[A-Z]+\/[A-Z]+', str(charting_symbol_content)).group()

    content = self.session.get("https://www.marketwatch.com/games/{}/tradeorder?chartingSymbol={}".format(self.game, charting_symbol, symbol), headers=self.headers).content
    parsed_data_attrs = BeautifulSoup(content, features='lxml').find('form').attrs  
    data = {
      'djid': parsed_data_attrs['data-djkey'],
      'ledgerId': parsed_data_attrs['data-pub'],
    }

    return data