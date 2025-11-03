import httpx
import time

#создание пользователя
create_user_payload = {
  "email": f"user.{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_data = create_user_response.json()


#создание кредитной карты
open_credit_card_account_payload = {
  "userId": create_user_data['user']['id']
}

open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account", json=open_credit_card_account_payload)
open_credit_card_account_data = open_credit_card_account_response.json()


#выполняем операцию
make_purchase_operation_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": open_credit_card_account_data['account']['cards'][0]['id'],
  "accountId": open_credit_card_account_data['account']['id'],
  "category": "taxi"
}

make_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=make_purchase_operation_payload)
make_purchase_operation_response_data = make_purchase_operation_response.json()


#получаем чек
get_purchase_operation_receipt = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{make_purchase_operation_response_data['operation']['id']}")
get_purchase_operation_receipt_data = get_purchase_operation_receipt.json()
print(get_purchase_operation_receipt_data)