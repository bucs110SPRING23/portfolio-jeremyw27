import json

def main():
    news = open("news.txt", "r").read().lower()
    sub_ftpr = open("subs.json", "r")
    json2python = json.load(sub_ftpr)

    for k, v in json2python.items():
        news = news.replace(k ,v)

    better_news = open("betternews.txt", "w")
    better_news.write(news)
    better_news.close()

main()