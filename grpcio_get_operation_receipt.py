# performance-tests/grpcio_get_operation_receipt.py

from __future__ import annotations

import grpc

from tools.fakers import fake

# --- Users ---

from contracts.services.gateway.users.rpc_create_user_pb2 import (
    CreateUserRequest,
    CreateUserResponse,
)
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import (
    UsersGatewayServiceStub,
)

# --- Accounts ---

from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse,
)
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import (
    AccountsGatewayServiceStub,
)

# --- Operations ---

from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse,
)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse,
)
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import (
    OperationsGatewayServiceStub,
)


GRPC_GATEWAY_ADDRESS = "localhost:9003"


def create_user(users_stub: UsersGatewayServiceStub) -> CreateUserResponse:
    """
    Создаёт нового пользователя через UsersGatewayService.CreateUser.
    Используем фейковые данные из tools.fakers.fake.
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
    Открывает дебетовый счёт через AccountsGatewayService.OpenDebitCardAccount.
    """
    request = OpenDebitCardAccountRequest(user_id=user_id)
    response: OpenDebitCardAccountResponse = accounts_stub.OpenDebitCardAccount(request)
    return response


def make_top_up_operation(
    operations_stub: OperationsGatewayServiceStub,
    account_id: str,
    card_id: str,
) -> MakeTopUpOperationResponse:
    """
    Выполняет операцию пополнения счёта через OperationsGatewayService.MakeTopUpOperation.

    Поля:
      - status: "COMPLETED"
      - amount: случайная сумма через fake.amount()
      - card_id: из ответа открытия счёта
      - account_id: из ответа открытия счёта
    """
    request = MakeTopUpOperationRequest(
        status="COMPLETED",
        amount=fake.amount(),
        card_id=card_id,
        account_id=account_id,
    )
    response: MakeTopUpOperationResponse = operations_stub.MakeTopUpOperation(request)
    return response


def get_operation_receipt(
    operations_stub: OperationsGatewayServiceStub,
    operation_id: str,
) -> GetOperationReceiptResponse:
    """
    Получает чек по операции через OperationsGatewayService.GetOperationReceipt.
    """
    # В большинстве контрактов тут поле обычно называется operation_id,
    # если у тебя в proto оно называется иначе (например, id) — просто поменяй имя аргумента.
    request = GetOperationReceiptRequest(operation_id=operation_id)
    response: GetOperationReceiptResponse = operations_stub.GetOperationReceipt(request)
    return response


def main() -> None:
    """
    Основной сценарий:
      1. Создаём пользователя.
      2. Открываем ему дебетовый счёт.
      3. Делаем операцию пополнения.
      4. Получаем чек по операции и выводим его.
    """
    with grpc.insecure_channel(GRPC_GATEWAY_ADDRESS) as channel:
        users_stub = UsersGatewayServiceStub(channel)
        accounts_stub = AccountsGatewayServiceStub(channel)
        operations_stub = OperationsGatewayServiceStub(channel)

        # 1. Создаём пользователя
        create_user_response = create_user(users_stub)
        print("Create user response:", create_user_response)

        user_id = create_user_response.user.id

        # 2. Открываем дебетовый счёт
        open_debit_account_response = open_debit_card_account(
            accounts_stub=accounts_stub,
            user_id=user_id,
        )
        print("Open debit card account response:", open_debit_account_response)

        account = open_debit_account_response.account
        account_id = account.id
        # Берем первую карту, как и в HTTP-примерах
        card_id = account.cards[0].id

        # 3. Выполняем операцию пополнения
        make_top_up_operation_response = make_top_up_operation(
            operations_stub=operations_stub,
            account_id=account_id,
            card_id=card_id,
        )
        print("Make top up operation response:", make_top_up_operation_response)

        operation_id = make_top_up_operation_response.operation.id

        # 4. Получаем чек по операции
        get_operation_receipt_response = get_operation_receipt(
            operations_stub=operations_stub,
            operation_id=operation_id,
        )
        print("Get operation receipt response:", get_operation_receipt_response)


if __name__ == "__main__":
    main()
