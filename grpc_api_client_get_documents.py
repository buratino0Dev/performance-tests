# performance-tests/grpc_api_client_get_documents.py

from __future__ import annotations

from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.documents.client import build_documents_gateway_grpc_client


def main() -> None:
    """
    gRPC-сценарий:
      1. Создать пользователя.
      2. Открыть кредитный счёт для этого пользователя.
      3. Получить документ тарифа.
      4. Получить документ контракта.
      5. Вывести все ответы в консоль.
    """

    # Инициализируем gRPC API-клиенты
    users_gateway_client = build_users_gateway_grpc_client()
    accounts_gateway_client = build_accounts_gateway_grpc_client()
    documents_gateway_client = build_documents_gateway_grpc_client()

    # 1. Создаём пользователя
    create_user_response = users_gateway_client.create_user()
    print("Create user response:", create_user_response)

    user_id = create_user_response.user.id

    # 2. Открываем кредитный счёт для этого пользователя
    open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(
        user_id=user_id,
    )
    print("Open credit card account response:", open_credit_card_account_response)

    account_id = open_credit_card_account_response.account.id

    # 3. Получаем документ тарифа по кредитному счёту
    get_tariff_document_response = documents_gateway_client.get_tariff_document(
        account_id=account_id,
    )
    print("Get tariff document response:", get_tariff_document_response)

    # 4. Получаем документ контракта по кредитному счёту
    get_contract_document_response = documents_gateway_client.get_contract_document(
        account_id=account_id,
    )
    print("Get contract document response:", get_contract_document_response)


if __name__ == "__main__":
    main()
