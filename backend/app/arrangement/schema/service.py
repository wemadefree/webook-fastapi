from typing import List, Optional
from sqlmodel import SQLModel

from app.arrangement.schema.organizations import OrganizationRead
from app.arrangement.schema.arrangements import ArrangementRead
from app.core.mixins import CamelCaseMixin


class ServiceTypeBase(SQLModel, CamelCaseMixin):
    name: str


class ServiceTypeCreate(ServiceTypeBase):
    pass


class ServiceTypeRead(ServiceTypeBase):
    id: int


class ServiceTypeUpdate(SQLModel):
    name: Optional[str] = None


class ServiceProviderBase(SQLModel, CamelCaseMixin):
    service_name: str
    service_type_id: Optional[int]
    organization_id: Optional[int]


class ServiceProviderCreate(ServiceProviderBase):
    pass


class ServiceProviderRead(ServiceProviderBase):
    id: int


class ServiceProviderUpdate(SQLModel):
    service_name: Optional[str]
    service_type_id: Optional[int]
    organization_id: Optional[int]


class ServiceProviderReadExtra(ServiceProviderRead):
    service_type: Optional[ServiceTypeRead]
    organization: Optional[OrganizationRead]


class LooseServiceRequisitionBase(SQLModel, CamelCaseMixin):
    comment: str
    arrangement_id: Optional[int]
    type_to_order_id: Optional[int]


class LooseServiceRequisitionRead(LooseServiceRequisitionBase):
    id: int


class LooseServiceRequisitionCreate(LooseServiceRequisitionBase):
    pass


class LooseServiceRequisitionUpdate(SQLModel, CamelCaseMixin):
    comment: Optional[str]
    arrangement_id: Optional[int]
    type_to_order_id: Optional[int]


class LooseServiceRequisitionReadExtra(LooseServiceRequisitionRead):
    arrangement: Optional[ArrangementRead]
    type_to_order: Optional[ServiceTypeRead]
