from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient

class GetOperationsQueryDict(TypedDict):

    """Структура данных для получения списка операций пользователя"""

    accountId: str

class GetOperationsSummaryQueryDict(TypedDict):

    """Структура данных для получения статистики операций пользователя"""

    accountId: str

class GetOperationsReceiptQueryDict(TypedDict):

        """Структура данных для получения чека по операции пользователя"""

        operation_id: str

class GetOperationQueryDict(TypedDict):

    """Структура данных для получения информации по операции пользователя"""

    operation_id: str

class MakeFeeOperationRequestDict(TypedDict):

    """Структура данных для создания запроса операции комиссии"""

  status: str
  amount: float
  cardId: str
  accountId: str

class MakeTopUpOperationRequestDict(TypedDict):

    """Структура данных для создания запроса операции пополнения"""

  status: str
  amount: float
  cardId: str
  accountId: str

class MakeCashbackOperationRequestDict(TypedDict):

    """Структура данных для создания запроса операции кэшбэка"""

  status: str
  amount: float
  cardId: str
  accountId: str

class MakeTransferOperationRequestDict(TypedDict):

    """Структура данных для создания запроса операции перевода"""

  status: str
  amount: float
  cardId: str
  accountId: str

class MakePurchaseOperationRequestDict(TypedDict):

    """Структура данных для создания запроса операции покупки"""

  status: str
  amount: float
  cardId: str
  accountId: str
  category: str

class MakeBillPaymentOperationRequestDict(TypedDict):

    """Структура данных для создания запроса операции оплаты по счету"""

  status: str
  amount: float
  cardId: str
  accountId: str

class MakeCashWithdrawalOperationRequestDict(TypedDict):

    """Структура данных для создания запроса операции снятия наличных"""

  status: str
  amount: float
  cardId: str
  accountId: str



class OperationsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с api/v1/operations сервиса http-gateway"""

    def get_operation_api(self, query: GetOperationQueryDict) -> Response:
        """Выполняет GET-запрос на получение информации по операции пользователя"""
        return self.get("/api/v1/operations", params=QueryParams(**query)))

    def get_operation_receipt_api(self, query: GetOperationReceiptQueryDict) -> Response:
        """Выполняет GET-запрос на получение чека по операции пользователя"""
        return self.get("/api/v1/operations-receipt", params=QueryParams(**query))


    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """Выполняет GET-запрос на получение информации по операциям пользователя"""
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operation_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """Выполняет GET-запрос на получение статистики операций пользователя"""
        return self.get("/api/v1/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции комиссии"""
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции пополнения"""
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции кэшбэка"""
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции перевода"""
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции покупки"""
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции оплаты по счету"""
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """Выполняет POST-запрос для создания операции снятия наличных"""
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)