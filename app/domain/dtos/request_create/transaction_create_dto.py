from pydantic import BaseModel
from typing import List

from ..transactions.customer_dto import CustomerDto
from ..transactions.payment_method_dto import PaymentMethodDto
from ..transactions.reference_dto import ReferenceDto
from ..transactions.items_dto import ItemDto

class TransactionCreateBodyDto(BaseModel):
    customer: CustomerDto
    amount: float
    payment_method: PaymentMethodDto
    reference: ReferenceDto
    items: List[ItemDto]