import requests

def fetch_cat_data():
    url = ("https://api.freeapi.app/api/v1/public/cats/cat/random")
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        name = user_data["name"]
        cat_description = user_data["description"]
        dog_friendly = user_data["dog_friendly"]
        life_span = user_data["life_span"]
        origin = user_data["origin"]
        return name , cat_description, dog_friendly,life_span,origin
    else:
        raise Exception("Failed to fetch data !")
    
def main():
    try:
        name, cat_description, dog_friendly, life_span, origin = fetch_cat_data()
        print(f"Name :{name} \nDescription :{cat_description} \nDog_friendly :{dog_friendly}\nLife_span :{life_span}\nOrigin :{origin} ")
    except Exception as e:
       print(str(e))  

if __name__ == "__main__":
    main()

        