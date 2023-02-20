import requests


baseUrl = "https://dummyjson.com/products"

resp = requests.get(baseUrl)

data = resp.json()
f = data['products']
user = input("What Do you need Sir? \n")


for models in f:
    if user in models['title']:
        print("Yes It is Available")
        print("Here are its Details")
        print(f"Name : {models['title']}")
        print(f"Description : {models['description']}")
        print(f"Price : {models['price']}")

if user not in models['title']:
    print("Sorry Not Available!")



