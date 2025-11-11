from clients.http.client import HTTPClient
from httpx import Response, Client
from typing import TypedDict

class IssueCardRequestDict(TypedDict):

    '''Структура данных для выпуска виртуальной и дебетовой карт'''

    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):

    '''Клиент для работы с /api/v1/cards'''

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:

        """Метод для создания виртуальных карт"""

        return self.post("api/v1/cards/issue-virtual-card", json=request)


    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:

        """Метод для создания физических карт"""

        return self.post("api/v1/cards/issue-physical-card", json=request)