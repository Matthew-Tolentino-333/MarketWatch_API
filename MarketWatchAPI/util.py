import requests
import json
import re

class MarketClient:
  def __init__(self):
    self.session = self.login('matttolent@gmail.com', 'money4me')
  
  def login(self, email, password):
    s = requests.Session()
    headers = {'Content-Type': 'application/json'}
    callback_headers = {'content-type': 'application/x-www-form-urlencoded'}
    payload = {
      'client_id': '5hssEAdMy0mJTICnJNvC9TXEw3Va7jfO',
      'connection': 'DJldap',
      'headers': {
        'X-REMOTE-USER': email
      },
      'nonce': '86614735-ebb3-4fc2-9674-d0bf0bf7fdc2',
      'ns': 'prod/accounts-mw',
      'password': password,
      'protocol': 'oauth2',
      'redirect_uri': "https://accounts.marketwatch.com/auth/sso/login",
      'response_type': "code",
      'scope': "openid idp_id roles email given_name family_name djid djUsername djStatus trackid tags prts suuid createTimestamp",
      'state': "hKFo2SBSS2c4UmprX3h0UDdZVEdvbVZldmJTdkhsaERkekxfSqFupWxvZ2luo3RpZNkgWjkyV0JFSHZvb1RhZ0VEbGYxb2Zla09TVk05WFRGVEijY2lk2SA1aHNzRUFkTXkwbUpUSUNuSk52QzlUWEV3M1ZhN2pmTw",
      'tenant': "sso",
      'ui_locales': "en-us-x-mw-3-8",
      'username': email,
      '_csrf': "sMAl0bPM-NtbjmegNoXqBRiNIQDvAYIWSEZc",
      '_intstate': "deprecated"
    }

    callback_payload = {
      'wa': 'wsignin1.0',
      'wresult': '',
      'wctx': {"strategy": "auth0",
       "auth0Client": "eyJuYW1lIjoiYXV0aDAuanMtdWxwIiwidmVyc2lvbiI6IjkuMTEuMyJ9",
       "tenant": "sso",
       "connection": "DJldap",
       "client_id": "5hssEAdMy0mJTICnJNvC9TXEw3Va7jfO",
       "response_type": "code",
       "scope": "openid idp_id roles email given_name family_name djid djUsername djStatus trackid tags prts suuid createTimestamp",
       "protocol": "oauth2",
       "redirect_uri": "https://accounts.marketwatch.com/auth/sso/login",
       "state": "hKFo2SB6T2RwamVOMmtUWTZ2bFFxQ1Z2VG8wWnl3TGQ3X2RXZ6FupWxvZ2luo3RpZNkgX0JZSXJwX1NTQ2FudXVGcVFFeXhlTzBEamN2a2lzMmSjY2lk2SA1aHNzRUFkTXkwbUpUSUNuSk52QzlUWEV3M1ZhN2pmTw",
       "nonce": "86614735-ebb3-4fc2-9674-d0bf0bf7fdc2",
       "sid": "I-l8WKkjyP5cp9yXwZ1vB-xMkvExlM_g", # var
       "realm": "DJldap"}
    }

    # Get state and csrf codes for login session
    res = s.get('https://accounts.marketwatch.com/login?target=https%3A%2F%2Fwww.marketwatch.com%2F')
    csrf = re.search("\=(\S*)", str(res.cookies)).group(1)
    state = re.search("(?<=\=)(.*?)(?=\&)", str(res.url)).group(1)

    payload['_csrf'] = csrf
    payload['state'] = state

    callback_payload['state'] = state

    # Attempt login
    try: 
      r = s.post('https://sso.accounts.dowjones.com/usernamepassword/login', headers=headers, json=payload)
      # r = s.post('https://sso.accounts.dowjones.com/usernamepassword/login', auth=(email, password))
      print(r.status_code)
      # print('--> content', r.text)
      print('--> headers', r.headers)
      # print('--> req headers', r.request.headers)

      # handle callback
      # r = s.get('https://www.marketwatch.com/games/marketbot')
      # print(r.status_code)
      # # print('--> content', r.text)
      # print('--> headers', r.headers)

    except BaseException as e:
      print('Problem with Login')
      print('Error: {}'.format(e))
      exit(1)

    # s.headers.update({'authorization': json.loads(r.content)['token']})
    return s

  def order(self):
    print('---> Ordering...')

    url = 'https://vse-api.marketwatch.com/v1/games/marketbot2/ledgers/aho-6WQuK9ud/trades'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'djid': "13-21983517",
        'expiresEndOfDay': 'false',
        'ledgerId': "aho-6WQuK9ud",
        'orderType': "Market",
        'shares': 50,
        'tradeType': "Buy",
    }
    
    try:
      res = self.session.post(url=url, headers=headers, json=payload)
      print(res.status_code)
      print('--> content', res.text)
      print('--> headers', res.headers)
    except Exception as e:
      print('Problem with Order')
      print('Error: {}'.format(e))
      exit(1)

