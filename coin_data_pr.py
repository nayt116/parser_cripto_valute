import requests
from bs4 import BeautifulSoup


def get_coin(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
    }

    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')

    coins = soup.find('tbody').find_all('tr')
    for coin in coins:
        coin_name = coin.find(class_='cmc-link').get('href').replace('/currencies/', '')[:-1]
        coin_price = coin.find(class_='sc-131di3y-0 cLgOOr')
        if coin_name:
            try:
                print(coin_name, coin_price.text)
            except:
                coin_price = coin.find_all('td')[-2].text
                print(coin_name, coin_price)


def main():
    get_coin(url='https://coinmarketcap.com')


if __name__=='__main__':
    main()