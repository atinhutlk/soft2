import requests

def get_random_chuck_norris_joke():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url)

    if response.status_code == 200:
        joke_data = response.json()
        joke_text = joke_data.get("value", "Failed to fetch Chuck Norris joke.")
        return joke_text
    else:
        return "Failed to fetch Chuck Norris joke."

if __name__ == "__main__":
    chuck_norris_joke = get_random_chuck_norris_joke()
    print(chuck_norris_joke)
