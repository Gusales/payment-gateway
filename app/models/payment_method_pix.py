import uuid

from sqlalchemy import Column, String, DateTime, Enum, Text
from sqlalchemy.sql import func

from app.config.database import Base
from app.domain.enums.payment_status import PaymentStatus

class PaymentMethodPix(Base):
    __tablename__ = "tb_payment_pix"

    id = Column("cod_payment_pix", String, nullable=False, unique=True, default=lambda: str(uuid.uuid4()), primary_key=True)
    code = Column("txt_paste_code", Text, nullable=False, unique=True)
    expiration_date = Column("dat_expiration_date", String, nullable=False)
    status = Column("txt_status_pix", Enum(PaymentStatus, name="enum_pix_status"), nullable=False, server_default=PaymentStatus.CREATED, default=PaymentStatus.CREATED)
    created_at = Column("dat_created_at", DateTime(timezone=True), nullable=False, default=func.now())