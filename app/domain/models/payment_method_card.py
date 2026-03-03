import uuid

from sqlalchemy import Column, String, DateTime, Enum, Text
from sqlalchemy.sql import func

from app.config.database import Base
from app.domain.enums.payment_status import PaymentStatus

class PaymentMethodCard(Base):
    __tablename__ = "tb_payment_card"

    id = Column("cod_payment_card", String, nullable=False, unique=True, default = lambda: str(uuid.uuid4()), primary_key=True)
    token = Column("txt_card_token", Text, nullable=False)
    last_numbers = Column("txt_last_numbers", String, nullable=False)
    card_brand = Column("txt_card_brand", String, nullable=False)
    holder_name = Column("txt_holder_name", String, nullable=False)
    expiration_month = Column("txt_expiration_month", String, nullable=False)
    expiration_year = Column("txt_expiration_year", String, nullable=False)
    status = Column("txt_status_card", Enum(PaymentStatus, name="enum_card_status"), nullable=False, server_default=PaymentStatus.CREATED, default=PaymentStatus.CREATED)
    created_at = Column("dat_created_at", DateTime(timezone=True), nullable=False, server_default=func.now())
