import requests

query= input("Enter the topic you want to search for: ")
api="your_api_key_here"

url =f"https://newsapi.org/v2/everything?q={query}&from=2026-03-26&sortBy=publishedAt&apiKey={api}"

print(url)

r=requests.get(url)

data=r.json()
articles=data["articles"]

for index, article in enumerate(articles):
    print(index+1)
    print(article["title"])
    print(article["url"])
    print("\n*****************************\n")