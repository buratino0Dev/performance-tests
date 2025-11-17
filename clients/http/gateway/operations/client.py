from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


# ====== Структуры данных ======

class GetOperationsQueryDict(TypedDict):
    """Структура данных для получения списка операций пользователя."""
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """Структура данных для получения статистики операций пользователя."""
    accountId: str


class GetOperationsReceiptQueryDict(TypedDict):
    """Структура данных для получения чека по операции пользователя."""
    operationId: str


class GetOperationQueryDict(TypedDict):
    """Структура данных для получения информации по операции пользователя."""
    operationId: str


class MakeFeeOperationRequestDict(TypedDict):
    """Структура данных для создания запроса операции комиссии."""
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationRequestDict(TypedDict):
    """Структура данных для создания запроса операции пополнения."""
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashbackOperationRequestDict(TypedDict):
    """Структура данных для создания запроса операции кэшбэка."""
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationRequestDict(TypedDict):
    """Структура данных для создания запроса операции перевода."""
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(TypedDict):
    """Структура данных для создания запроса операции покупки."""
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str


class MakeBillPaymentOperationRequestDict(TypedDict):
    """Структура данных для создания запроса операции оплаты по счету."""
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """Структура данных для создания запроса операции снятия наличных."""
    status: str
    amount: float
    cardId: str
    accountId: str


# ====== Структуры ответов ======

class OperationDict(TypedDict):
    """
    Структура операции.

    Пример:
    {
      "id": "string",
      "type": "FEE",
      "status": "FAILED",
      "amount": 0,
      "cardId": "string",
      "category": "string",
      "createdAt": "2025-06-08T06:50:17.124Z",
      "accountId": "string"
    }
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Структура чека операции.

    {
      "url": "https://example.com/",
      "document": "string"
    }
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    Структура статистики операций.

    {
      "spentAmount": 0,
      "receivedAmount": 0,
      "cashbackAmount": 0
    }
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationResponseDict(TypedDict):
    operation: OperationDict


class GetOperationReceiptResponseDict(TypedDict):
    receipt: OperationReceiptDict


class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict


class MakeFeeOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    operation: OperationDict


# ====== Клиент ======

class OperationsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/operations сервиса http-gateway."""

    # --- Низкоуровневые методы (работают с Response) ---

    def get_operation_api(self, query: GetOperationQueryDict) -> Response:
        """Выполняет GET-запрос на получение информации по операции пользователя."""
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operation_receipt_api(self, query: GetOperationsReceiptQueryDict) -> Response:
        """Выполняет GET-запрос на получение чека по операции пользователя."""
        return self.get("/api/v1/operations-receipt", params=QueryParams(**query))

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """Выполняет GET-запрос на получение информации по операциям пользователя."""
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """Выполняет GET-запрос на получение статистики операций пользователя."""
        return self.get("/api/v1/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции комиссии."""
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции пополнения."""
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции кэшбэка."""
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции перевода."""
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции покупки."""
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции оплаты по счету."""
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции снятия наличных."""
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    # --- Высокоуровневые методы (работают с dict’ами) ---

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получить информацию по конкретной операции.

        :param operation_id: Идентификатор операции.
        """
        query = GetOperationQueryDict(operationId=operation_id)
        response = self.get_operation_api(query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        """
        query = GetOperationsReceiptQueryDict(operationId=operation_id)
        response = self.get_operation_receipt_api(query)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получить список операций по счёту.

        :param account_id: Идентификатор счёта.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получить статистику операций по счёту.

        :param account_id: Идентификатор счёта.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Создать операцию комиссии.

        Для примера используем фиксированные статус и сумму.
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Создать операцию пополнения счёта.

        Для примера используем фиксированную сумму, как в задании.
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=1500.11,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """Создать операцию кэшбэка."""
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=100.0,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """Создать операцию перевода."""
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=500.0,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        """Создать операцию покупки."""
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=999.99,
            cardId=card_id,
            accountId=account_id,
            category="products",
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """Создать операцию оплаты по счёту."""
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=777.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """Создать операцию снятия наличных."""
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=300.0,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


# ====== Builder ======

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
