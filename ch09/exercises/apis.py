import requests

def main():
    x = int(input('Enter a number between 1 and 30 for an NBA team: '))
    r = requests.get('https://www.balldontlie.io/api/v1/teams')
    info = r.json()
    info = info['data'][x-1]
    for _ in info:
        print(_, ':', info.get(_))

main()
