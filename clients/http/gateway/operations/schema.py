from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl, ConfigDict

from tools.fakers import fake


class BaseSchema(BaseModel):
    """
    Базовая схема с общими настройками.
    """
    model_config = ConfigDict(populate_by_name=True)


# === ENUM'ы ===

class OperationType(str, Enum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    PURCHASE = "PURCHASE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    # при необходимости можно добавить другие статусы


# === Основные сущности ===

class OperationSchema(BaseSchema):
    """
    Описание структуры операции.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseSchema):
    """
    Описание структуры чека по операции.
    """
    url: HttpUrl
    document: str


class OperationsSummarySchema(BaseSchema):
    """
    Описание структуры статистики по операциям.
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


# === Запросы (query) ===

class GetOperationsQuerySchema(BaseSchema):
    """
    Структура query параметров запроса для получения списка операций по счёту.
    """
    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseSchema):
    """
    Структура query параметров запроса для получения статистики по операциям счёта.
    """
    account_id: str = Field(alias="accountId")


# === Обёртки ответов ===

class GetOperationResponseSchema(BaseSchema):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationSchema


class GetOperationsResponseSchema(BaseSchema):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseSchema):
    """
    Описание структуры ответа получения статистики по операциям.
    """
    summary: OperationsSummarySchema


class GetOperationReceiptResponseSchema(BaseSchema):
    """
    Описание структуры ответа получения чека по операции.
    """
    receipt: OperationReceiptSchema


# === Тела запросов на создание операций ===

class MakeOperationRequestSchema(BaseSchema):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    # Автоматическая генерация статуса и суммы
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)

    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции покупки.

    Дополнительное поле:
    - category: категория покупки.
    """
    category: str = Field(default_factory=fake.category)


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции оплаты по счёту.
    """
    pass


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции снятия наличных.
    """
    pass


# === Обёртки ответов на создание операций ===

class MakeFeeOperationResponseSchema(BaseSchema):
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseSchema):
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseSchema):
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseSchema):
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseSchema):
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseSchema):
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseSchema):
    operation: OperationSchema
