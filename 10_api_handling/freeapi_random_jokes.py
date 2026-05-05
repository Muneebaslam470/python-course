import requests

def fetch_random_joke_api():
    url = ("https://api.freeapi.app/api/v1/public/randomjokes/joke/random")
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        random_joke = user_data["content"]
        message = data["message"]
        return random_joke, message
    else:
        raise Exception("Failed to fetch data")
    
def main():
    try:
        random_joke , message = fetch_random_joke_api()
        print(f"Joke : {random_joke} \n Message : {message}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
     main()
