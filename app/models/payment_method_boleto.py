import uuid

from sqlalchemy import Column, String, DateTime, Enum, Text
from sqlalchemy.sql import func

from app.config.database import Base
from app.domain.enums.payment_status import PaymentStatus

class PaymentMethodBoleto(Base):
    __tablename__ = "tb_payment_boleto"

    id = Column("cod_payment_boleto", String, nullable=False, unique=True, default=lambda: str(uuid.uuid4()), primary_key=True)
    code = Column("cod_boleto_code", Text, nullable=False, unique=True)
    bar_code = Column("cod_boleto_barcode", Text, nullable=False, unique=True)
    due_date = Column("dat_due_date", DateTime(timezone=True), nullable=False)
    status = Column("txt_status_boleto", Enum(PaymentStatus, name="enum_card_status"), nullable=False, server_default=PaymentStatus.CREATED, default=PaymentStatus.CREATED)
    created_at = Column("dat_created_at", DateTime(timezone=True), nullable=False, server_default=func.now())
