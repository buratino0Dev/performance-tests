from __future__ import annotations

from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from tools.fakers import fake

# ---- gRPC-контракты OperationsGatewayService ----

# Получение операции
from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse,
)

# Получение чека по операции
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse,
)

# Получение списка операций
from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse,
)

# Получение статистики по операциям
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse,
)

# Создание операций
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse,
)

# Enum статуса операции (импортируй из того pb2, где он реально объявлен)
from contracts.services.gateway.operations.operations_pb2 import OperationStatus

# Стаб сервиса
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import (
    OperationsGatewayServiceStub,
)


class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.

    Предоставляет низкоуровневые *_api методы (прямые вызовы gRPC)
    и высокоуровневые обёртки, работающие со строковыми идентификаторами
    и фейковыми данными.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к grpc-gateway.
        """
        super().__init__(channel)
        self.stub = OperationsGatewayServiceStub(channel)

    # ---------- Низкоуровневые методы (прямые gRPC-вызовы) ----------

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.GetOperation.

        :param request: gRPC-запрос с идентификатором операции.
        :return: gRPC-ответ с данными операции.
        """
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(
        self,
        request: GetOperationReceiptRequest,
    ) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.GetOperationReceipt.

        :param request: gRPC-запрос с идентификатором операции.
        :return: gRPC-ответ с данными чека по операции.
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.GetOperations.

        :param request: gRPC-запрос с идентификатором счёта.
        :return: gRPC-ответ со списком операций.
        """
        return self.stub.GetOperations(request)

    def get_operations_summary_api(
        self,
        request: GetOperationsSummaryRequest,
    ) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.GetOperationsSummary.

        :param request: gRPC-запрос с идентификатором счёта.
        :return: gRPC-ответ со сводной статистикой операций.
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(
        self,
        request: MakeFeeOperationRequest,
    ) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.MakeFeeOperation.

        :param request: gRPC-запрос с параметрами операции комиссии.
        :return: gRPC-ответ с данными созданной операции.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(
        self,
        request: MakeTopUpOperationRequest,
    ) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.MakeTopUpOperation.

        :param request: gRPC-запрос с параметрами операции пополнения.
        :return: gRPC-ответ с данными созданной операции.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(
        self,
        request: MakeCashbackOperationRequest,
    ) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.MakeCashbackOperation.

        :param request: gRPC-запрос с параметрами операции кэшбэка.
        :return: gRPC-ответ с данными созданной операции.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(
        self,
        request: MakeTransferOperationRequest,
    ) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.MakeTransferOperation.

        :param request: gRPC-запрос с параметрами операции перевода.
        :return: gRPC-ответ с данными созданной операции.
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(
        self,
        request: MakePurchaseOperationRequest,
    ) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.MakePurchaseOperation.

        :param request: gRPC-запрос с параметрами операции покупки.
        :return: gRPC-ответ с данными созданной операции.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(
        self,
        request: MakeBillPaymentOperationRequest,
    ) -> MakeBillPaymentOperationResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.MakeBillPaymentOperation.

        :param request: gRPC-запрос с параметрами операции оплаты по счёту.
        :return: gRPC-ответ с данными созданной операции.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(
        self,
        request: MakeCashWithdrawalOperationRequest,
    ) -> MakeCashWithdrawalOperationResponse:
        """
        Низкоуровневый вызов OperationsGatewayService.MakeCashWithdrawalOperation.

        :param request: gRPC-запрос с параметрами операции снятия наличных.
        :return: gRPC-ответ с данными созданной операции.
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    # ---------- Высокоуровневые методы-обёртки ----------

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """
        Получить информацию об операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ gRPC-сервиса с данными операции.
        """
        request = GetOperationRequest(operation_id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Получить чек по заданной операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ gRPC-сервиса с данными чека по операции.
        """
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """
        Получить список операций по указанному счёту.

        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса со списком операций.
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Получить сводную статистику операций по указанному счёту.

        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса с агрегированной статистикой.
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """
        Создать операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса с данными созданной операции.
        """
        request = MakeFeeOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTopUpOperationResponse:
        """
        Создать операцию пополнения счёта.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса с данными созданной операции.
        """
        request = MakeTopUpOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashbackOperationResponse:
        """
        Создать операцию кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса с данными созданной операции.
        """
        request = MakeCashbackOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTransferOperationResponse:
        """
        Создать операцию перевода средств.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта-источника.
        :return: Ответ gRPC-сервиса с данными созданной операции.
        """
        request = MakeTransferOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakePurchaseOperationResponse:
        """
        Создать операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса с данными созданной операции.
        """
        request = MakePurchaseOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
            category=fake.category(),
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeBillPaymentOperationResponse:
        """
        Создать операцию оплаты по счёту.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса с данными созданной операции.
        """
        request = MakeBillPaymentOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashWithdrawalOperationResponse:
        """
        Создать операцию снятия наличных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса с данными созданной операции.
        """
        request = MakeCashWithdrawalOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания OperationsGatewayGRPCClient.

    Использует общий билдер gRPC-канала build_gateway_grpc_client().

    :return: Инициализированный gRPC-клиент для OperationsGatewayService.
    """
    channel = build_gateway_grpc_client()
    return OperationsGatewayGRPCClient(channel=channel)
