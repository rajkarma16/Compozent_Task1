import requests

def quote():
    url = "https://quoteapi.pythonanywhere.com/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        return None

def display(data):
    if data and "Quotes" in data:
        for item in data["Quotes"]:
            quote = item.get("quote")
            author = item.get("author")
            print(f"\"{quote}\"")
            print(f"- {author}")
    else:
        print("No quote available.")

quote_data = quote()
display(quote_data)

