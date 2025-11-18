# performance-tests/grpcio_open_debit_card_account.py

from __future__ import annotations

import grpc

from tools.fakers import fake

# Импорты для UsersGatewayService
from contracts.services.gateway.users.rpc_create_user_pb2 import (
    CreateUserRequest,
    CreateUserResponse,
)
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import (
    UsersGatewayServiceStub,
)

# Импорты для AccountsGatewayService
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse,
)
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import (
    AccountsGatewayServiceStub,
)


GRPC_GATEWAY_ADDRESS = "localhost:9003"


def create_user(users_stub: UsersGatewayServiceStub) -> CreateUserResponse:
    """
    Создаёт нового пользователя через UsersGatewayService.CreateUser.
    Используем генератор фейковых данных fake.
    """
    request = CreateUserRequest(
        email=fake.email(),
        last_name=fake.last_name(),
        first_name=fake.first_name(),
        middle_name=fake.middle_name(),
        phone_number=fake.phone_number(),
    )

    response: CreateUserResponse = users_stub.CreateUser(request)
    return response


def open_debit_card_account(
    accounts_stub: AccountsGatewayServiceStub,
    user_id: str,
) -> OpenDebitCardAccountResponse:
    """
    Открывает дебетовый аккаунт для пользователя
    через AccountsGatewayService.OpenDebitCardAccount.
    """
    request = OpenDebitCardAccountRequest(user_id=user_id)
    response: OpenDebitCardAccountResponse = accounts_stub.OpenDebitCardAccount(request)
    return response


def main() -> None:
    """
    Основной сценарий:
    1. Открыть канал к grpc-gateway.
    2. Создать пользователя.
    3. Открыть дебетовый счёт.
    4. Вывести оба ответа в консоль.
    """
    with grpc.insecure_channel(GRPC_GATEWAY_ADDRESS) as channel:
        users_stub = UsersGatewayServiceStub(channel)
        accounts_stub = AccountsGatewayServiceStub(channel)

        # 1. Создание пользователя
        create_user_response = create_user(users_stub)
        print("Create user response:", create_user_response)

        user_id = create_user_response.user.id

        # 2. Открытие дебетового счёта
        open_debit_account_response = open_debit_card_account(
            accounts_stub=accounts_stub,
            user_id=user_id,
        )
        print("Open debit card account response:", open_debit_account_response)


if __name__ == "__main__":
    main()
