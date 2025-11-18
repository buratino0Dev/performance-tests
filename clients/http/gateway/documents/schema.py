from pydantic import BaseModel, HttpUrl, ConfigDict


class DocumentSchema(BaseModel):
    """
    Модель документа.
    """
    model_config = ConfigDict(populate_by_name=True)

    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Модель ответа для документа тарифа.
    """
    model_config = ConfigDict(populate_by_name=True)

    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Модель ответа для документа контракта.
    """
    model_config = ConfigDict(populate_by_name=True)

    contract: DocumentSchema
