import httpx
import time


#Тело запроса на создание пользователя
create_user_payload = {
  "email": f"user.{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

#Создаем пользователя и вытаскиваем userId
user_create_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
user_create_data = user_create_response.json()
user_id = user_create_data['user']['id']
print("Статус код создания пользователя:", user_create_response.status_code)
print("Данные пользователя в формате json:", user_create_data)

#Тело запроса создания банковского счета с полученным айди
open_deposit_account_payload = {
  "userId": user_id
}

#Создаем счет и вытаскиваем нужные данные
open_deposit_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=open_deposit_account_payload)
open_deposit_account_data = open_deposit_account_response.json()
print("Статус код создания банковского счета:", open_deposit_account_response.status_code)
print("Данные банковского счета:", open_deposit_account_data)
