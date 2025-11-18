from __future__ import annotations

from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client

# gRPC-контракты для CardsGatewayService
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import (
    IssueVirtualCardRequest,
    IssueVirtualCardResponse,
)
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import (
    IssuePhysicalCardRequest,
    IssuePhysicalCardResponse,
)
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import (
    CardsGatewayServiceStub,
)


class CardsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с CardsGatewayService.
    Предоставляет методы для выпуска виртуальных и физических карт.
    """

    def __init__(self, channel: Channel):
        """
        Инициализирует клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к grpc-gateway.
        """
        super().__init__(channel)
        # gRPC-стаб, сгенерированный из .proto
        self.stub = CardsGatewayServiceStub(channel)

    # ---------- Низкоуровневые методы (прямые gRPC-вызовы) ----------

    def issue_virtual_card_api(
        self,
        request: IssueVirtualCardRequest,
    ) -> IssueVirtualCardResponse:
        """
        Низкоуровневый вызов метода IssueVirtualCard.

        :param request: gRPC-модель запроса IssueVirtualCardRequest.
        :return: gRPC-модель ответа IssueVirtualCardResponse.
        """
        return self.stub.IssueVirtualCard(request)

    def issue_physical_card_api(
        self,
        request: IssuePhysicalCardRequest,
    ) -> IssuePhysicalCardResponse:
        """
        Низкоуровневый вызов метода IssuePhysicalCard.

        :param request: gRPC-модель запроса IssuePhysicalCardRequest.
        :return: gRPC-модель ответа IssuePhysicalCardResponse.
        """
        return self.stub.IssuePhysicalCard(request)

    # ---------- Высокоуровневые методы-обёртки ----------

    def issue_virtual_card(
        self,
        user_id: str,
        account_id: str,
    ) -> IssueVirtualCardResponse:
        """
        Выпускает виртуальную карту для указанного пользователя и счёта.

        :param user_id: Идентификатор пользователя.
        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса с данными выпущенной карты.
        """
        request = IssueVirtualCardRequest(
            user_id=user_id,
            account_id=account_id,
        )
        return self.issue_virtual_card_api(request)

    def issue_physical_card(
        self,
        user_id: str,
        account_id: str,
    ) -> IssuePhysicalCardResponse:
        """
        Выпускает физическую карту для указанного пользователя и счёта.

        :param user_id: Идентификатор пользователя.
        :param account_id: Идентификатор счёта.
        :return: Ответ gRPC-сервиса с данными выпущенной карты.
        """
        request = IssuePhysicalCardRequest(
            user_id=user_id,
            account_id=account_id,
        )
        return self.issue_physical_card_api(request)


def build_cards_gateway_grpc_client() -> CardsGatewayGRPCClient:
    """
    Фабричная функция для создания экземпляра CardsGatewayGRPCClient.

    Использует общий билдер gRPC-канала build_gateway_grpc_client().

    :return: Инициализированный CardsGatewayGRPCClient.
    """
    channel = build_gateway_grpc_client()
    return CardsGatewayGRPCClient(channel=channel)
