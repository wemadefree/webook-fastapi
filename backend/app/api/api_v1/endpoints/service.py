from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import LooseServiceRequisition, ServiceType, ServiceProvider
from app.arrangement.schema.service import LooseServiceRequisitionRead, LooseServiceRequisitionReadExtra, LooseServiceRequisitionCreate, LooseServiceRequisitionUpdate, ServiceTypeRead, ServiceTypeCreate, ServiceTypeUpdate, ServiceProviderRead, ServiceProviderReadExtra, ServiceProviderCreate, ServiceProviderUpdate
from app.arrangement.factory import CrudManager

service_router = ser = APIRouter()


@ser.post("/servicetypes", response_model=ServiceTypeRead)
def create_servicetype(*, session: Session = Depends(get_session), servicetype: ServiceTypeCreate):
    servicetype_item = CrudManager(ServiceType).create_item(session, servicetype)
    return servicetype_item


@ser.get("/servicetypes", response_model=List[ServiceTypeRead])
def read_servicetypes(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    servicetypes = CrudManager(ServiceType).read_items(session, offset, limit)
    return servicetypes


@ser.get("/servicetype/{servicetype_id}", response_model=ServiceTypeRead)
def read_servicetype(*, session: Session = Depends(get_session), servicetype_id: int):
    servicetype_item = CrudManager(ServiceType).read_item(session, servicetype_id)
    return servicetype_item


@ser.patch("/servicetype/{servicetype_id}", response_model=ServiceTypeRead)
def update_servicetype(*, session: Session = Depends(get_session), servicetype_id: int, servicetype: ServiceTypeUpdate):
    servicetype_item = CrudManager(ServiceType).edit_item(session, servicetype_id, servicetype)
    return servicetype_item


@ser.delete("/servicetype/{servicetype_id}")
def delete_servicetype(*, session: Session = Depends(get_session), servicetype_id: int):
    return CrudManager(ServiceType).delete_item(session, servicetype_id)


@ser.post("/serviceproviders", response_model=ServiceProviderRead)
def create_serviceprovider(*, session: Session = Depends(get_session), serviceprovider: ServiceProviderCreate):
    serviceprovider_item = CrudManager(ServiceProvider).create_item(session, serviceprovider)
    return serviceprovider_item


@ser.get("/serviceproviders", response_model=List[ServiceProviderRead])
def read_serviceproviders(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    serviceproviders = CrudManager(ServiceProvider).read_items(session, offset, limit)
    return serviceproviders


@ser.get("/serviceprovider/{serviceprovider_id}", response_model=ServiceProviderReadExtra)
def read_serviceprovider(*, session: Session = Depends(get_session), serviceprovider_id: int):
    serviceprovider_item = CrudManager(ServiceProvider).read_item(session, serviceprovider_id)
    return serviceprovider_item


@ser.patch("/serviceprovider/{serviceprovider_id}", response_model=ServiceProviderReadExtra)
def update_serviceprovider(*, session: Session = Depends(get_session), serviceprovider_id: int, serviceprovider: ServiceProviderUpdate):
    serviceprovider_item = CrudManager(ServiceProvider).edit_item(session, serviceprovider_id, serviceprovider)
    return serviceprovider_item


@ser.delete("/serviceprovider/{serviceprovider_id}")
def delete_serviceprovider(*, session: Session = Depends(get_session), serviceprovider_id: int):
    return CrudManager(ServiceProvider).delete_item(session, serviceprovider_id)


@ser.post("/servicerequisitons", response_model=LooseServiceRequisitionReadExtra)
def create_servicerequisiton(*, session: Session = Depends(get_session), servicerequisiton: LooseServiceRequisitionCreate):
    servicerequisiton_item = CrudManager(LooseServiceRequisition).create_item(session, servicerequisiton)
    return servicerequisiton_item


@ser.get("/servicerequisitons", response_model=List[LooseServiceRequisitionRead])
def read_servicerequisitons(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    servicerequisitons = CrudManager(LooseServiceRequisition).read_items(session, offset, limit)
    return servicerequisitons


@ser.get("/servicerequisiton/{servicerequisiton_id}", response_model=LooseServiceRequisitionReadExtra)
def read_servicerequisiton(*, session: Session = Depends(get_session),servicerequisiton_id: int):
    servicerequisiton_item = CrudManager(LooseServiceRequisition).read_item(session, servicerequisiton_id)
    return servicerequisiton_item


@ser.patch("/servicerequisiton/{servicerequisiton_id}", response_model=LooseServiceRequisitionReadExtra)
def update_servicerequisiton(*, session: Session = Depends(get_session), servicerequisiton_id: int, servicerequisiton: LooseServiceRequisitionUpdate):
    servicerequisiton_item = CrudManager(LooseServiceRequisition).edit_item(session, servicerequisiton_id, servicerequisiton)
    return servicerequisiton_item


@ser.delete("/servicerequisiton/{servicerequisiton_id}")
def delete_servicerequisiton(*, session: Session = Depends(get_session), servicerequisiton_id: int):
    return CrudManager(LooseServiceRequisition).delete_item(session, servicerequisiton_id)
