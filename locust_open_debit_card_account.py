from locust import HttpUser, between, task
from tools.fakers import fake

class OpenDebitCardAccountScenarioUser(HttpUser):

    wait_time = between(1, 3)
    user_data = dict


    def on_start(self) -> None:
      request = {
        "email": fake.email(),
        "lastName": fake.last_name(),
        "firstName": fake.first_name(),
        "middleName": fake.middle_name(),
        "phoneNumber": fake.phone_number()
    }
      response = self.client.post("/api/v1/users", json=request)

    # Сохраняем полученные данные, включая ID пользователя
      self.user_data = response.json()


    @task
    def open_debit_card_account(self):
      open_debit_card_account_request = {"userId": self.user_data['user']['id']}
      self.client.post("/api/v1/accounts/open-debit-card-account", json=open_debit_card_account_request)
