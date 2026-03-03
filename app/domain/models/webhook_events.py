import uuid

from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB

from app.config.database import Base
from app.domain.enums.accept_provider_names import AcceptProviderNames

class WebhookEvent(Base):
    __tablename__ = "tb_webhook_events"

    id = Column("cod_webhook_event", String, nullable=False, unique=True, default=lambda: str(uuid.uuid4()), primary_key=True)
    provider_name = Column("txt_provider_name", Enum(AcceptProviderNames, name="enum_provider_transaction_name", create_type=False), nullable=False, server_default=AcceptProviderNames.MOCK.name, default=AcceptProviderNames.MOCK)
    provider_event_id = Column("cod_provider_event", String, nullable=False)
    event_type = Column("txt_event_type", String, nullable=False)
    payment_id = Column("cod_payment_id", ForeignKey("tb_payments.cod_payment_id"))
    payload = Column("txt_payload_content", JSONB, nullable=False)
    received_at = Column("dat_received_at", DateTime(timezone=True), nullable=False, server_default=func.now())