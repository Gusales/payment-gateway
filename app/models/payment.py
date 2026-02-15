import uuid

from sqlalchemy import Column, String, Numeric, Text, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from app.domains.enums.reference_type import ReferenceType
from app.domains.enums.payment_method_type import PaymentMethodType
from app.domains.enums.payment_status import PaymentStatus

from app.config.database import Base

class Payment(Base):
    __tablename__ = "tb_payments"

    id = Column("cod_payment_id", String, nullable=False, unique=True, default=lambda: str(uuid.uuid4()), primary_key=True)
    idempotency_key = Column("cod_idempotency_key", String, nullable=False, unique=True)
    customer_id = Column("cod_customer_id", String, nullable=False)
    customer_name = Column("txt_customer_name", String, nullable=False)
    customer_document = Column("txt_customer_document", String, nullable=False)
    customer_email = Column("txt_customer_email", String, nullable=False)
    reference_type = Column("txt_reference_type", Enum(ReferenceType, name="enum_reference_type"), nullable=False)
    reference_id = Column("cod_reference_id", String, nullable=False)
    amount = Column("int_total_amount", Numeric(precision=12, scale=2), nullable=False)
    payment_method_type = Column("txt_payment_method", Enum(PaymentMethodType, name="enum_payment_method_type"), nullable=False)
    payment_status = Column("txt_payment_status", Enum(PaymentStatus, name="enum_payment_status"), nullable=False)
    items_snapshot = Column("txt_items_snapshot", Text, nullable=True)
    created_at = Column("dat_created_at", DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column("dat_updated_at", DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    def __init__(self, idempotency_key, customer_id, customer_name, customer_document, customer_email, reference_type, reference_id, amount, payment_method_type, payment_status, items_snapshot = None):
        self.idempotency_key = idempotency_key
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_document = customer_document
        self.customer_email = customer_email
        self.reference_type = reference_type
        self.reference_id = reference_id
        self.amount = amount
        self.payment_method_type = payment_method_type
        self.payment_status = payment_status
        self.items_snapshot = items_snapshot