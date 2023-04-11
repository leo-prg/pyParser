import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.binance.com/en/markets')
soup = BeautifulSoup(response.content, 'html.parser')
market_container = soup.find('div', {'class': 'css-1vuj9rf'})
markets = market_container.findAll('div', {'class': 'css-leyy1t'})
for market in markets[0:100]:  # Выбираем первые 100 криптовалют
    symbol = market.find('div', {'class': 'css-1x8dg53'}).text.strip()
    price  = market.find('div', {'class': 'css-ovtrou'}).text.strip()
    if market.find('div', {'class': 'css-1vgqjs4'}) is not None:
        change = market.find('div', {'class': 'css-1vgqjs4'}).text.strip()
    elif market.find('div', {'class': 'css-1ca67uc'}) is not None:
        change = market.find('div', {'class': 'css-1ca67uc'}).text.strip()
    volume = market.find('div', {'class': 'css-s779xv'}).text.strip()
    print(symbol, price, change, volume)
