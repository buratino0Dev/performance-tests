# performance-tests/grpc_api_client_make_top_up_operation.py

from __future__ import annotations

from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client


def main() -> None:
    """
    gRPC-сценарий:
      1. Создать пользователя.
      2. Открыть дебетовый счёт для этого пользователя.
      3. Создать операцию пополнения дебетового счёта.
      4. Вывести все ответы в консоль.
    """

    # Инициализируем gRPC API-клиенты
    users_gateway_client = build_users_gateway_grpc_client()
    accounts_gateway_client = build_accounts_gateway_grpc_client()
    operations_gateway_client = build_operations_gateway_grpc_client()

    # 1. Создаём пользователя
    create_user_response = users_gateway_client.create_user()
    print("Create user response:", create_user_response)

    user_id = create_user_response.user.id

    # 2. Открываем дебетовый счёт для этого пользователя
    # (в задании опечатка в названии метода, нам нужен именно debit)
    open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
        user_id=user_id,
    )
    print("Open debit card account response:", open_debit_card_account_response)

    account = open_debit_card_account_response.account
    account_id = account.id

    # Берём первую карту счёта (как и в предыдущих заданиях)
    card_id = account.cards[0].id

    # 3. Создаём операцию пополнения дебетового счёта
    make_top_up_operation_response = operations_gateway_client.make_top_up_operation(
        card_id=card_id,
        account_id=account_id,
    )
    print("Make top up operation response:", make_top_up_operation_response)


if __name__ == "__main__":
    main()
