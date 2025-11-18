from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.documents.schema import (
    GetTariffDocumentResponseSchema,
    GetContractDocumentResponseSchema,
)


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    # --- Низкоуровневые методы (работают с httpx.Response) ---

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить документ тарифа по счету (низкоуровневый метод).

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить документ контракта по счету (низкоуровневый метод).

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    # --- Высокоуровневые методы (возвращают Pydantic-модели) ---

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseSchema:
        """
        Высокоуровневый метод получения документа тарифа по счёту.

        :param account_id: Идентификатор счёта.
        :return: Pydantic-модель с данными документа тарифа.
        """
        response = self.get_tariff_document_api(account_id)
        # Используем Pydantic v2: model_validate_json вместо response.json()
        return GetTariffDocumentResponseSchema.model_validate_json(response.text)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseSchema:
        """
        Высокоуровневый метод получения документа контракта по счёту.

        :param account_id: Идентификатор счёта.
        :return: Pydantic-модель с данными документа контракта.
        """
        response = self.get_contract_document_api(account_id)
        return GetContractDocumentResponseSchema.model_validate_json(response.text)


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
