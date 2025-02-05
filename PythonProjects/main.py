import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '101d7c54fc55eef99482b8a0ca3015e9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }

body_registration = {
    "trainer_token": TOKEN,
    "email": "suleimanov.ruslan2017@mail.ru",
    "password": "Iloveqa1111"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation) 
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response_create.text)

message = response_create.json()['message']
print(message)