import uuid

from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func

from app.config.database import Base

from app.domain.enums.accept_provider_names import AcceptProviderNames
from app.domain.enums.provider_status import ProviderStatus

class ProviderTransactions(Base):
    __tablename__ = 'tb_provider_transactions'

    id = Column("cod_provider_transaction", String, nullable=False, unique=True, default=lambda: str(uuid.uuid4()), primary_key=True)
    payment_id = Column("cod_fk_payment_id", ForeignKey("tb_payments.cod_payment_id"))
    provider_name = Column("txt_provider_name", Enum(AcceptProviderNames, name="enum_provider_transaction_name"), nullable=False)
    provider_id = Column("cod_provider_id", String, nullable=False)
    provider_status = Column("txt_provider_status", Enum(ProviderStatus, name="enum_provider_transaction_status"), nullable=False, server_default=ProviderStatus.PENDING, default=ProviderStatus.PENDING)
    error_code = Column("txt_error_code", String, nullable=True)
    error_message = Column("txt_error_message", String, nullable=True)
    created_at = Column("dat_created_at", DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column("dat_updated_at", DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())