# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    bitcoins = get_bitcoins_amount()
    dollars = convert_bitcoins_to_dollars(bitcoins)
    display_results(bitcoins, dollars)


def get_bitcoins_amount():
    while True:
        try:
            bitcoins = float(input('Enter the number of bitcoin: '))
            if bitcoins >= 0:
                return bitcoins
            else:
                print(' Please enter a number greater than 0')
        except ValueError:
            print('Enter a positive number.')


def convert_bitcoins_to_dollars(bitcoins):
    rate_json = get_bitcoins_data()
    exchange_rate = extract_rate(rate_json)

    bitcoins = exchange_rate * bitcoins
    return bitcoins


# this function will be mocked
def get_bitcoins_data():
    return requests.get(url).json()


def extract_rate(rate_json):
    return rate_json['bpi']['USD']['rate_float']


def display_results(bitcoins, dollars):
    print(f'{bitcoins} bitcoin is equal to ${dollars}')


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
