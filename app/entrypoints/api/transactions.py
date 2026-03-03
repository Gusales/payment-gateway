from fastapi import Depends, status

from app.domain.http.router import router
from app.domain.dtos.request_create.transaction_create_dto import TransactionCreateBodyDto
from app.entrypoints.pipes.validate_x_idempotency_key import validate_x_idempotency_key

@router.post(
        "/transactions",
        status_code=status.HTTP_201_CREATED,
        tags=["Transactions"],
        dependencies=[Depends(validate_x_idempotency_key)]
    )
def create_transaction(body: TransactionCreateBodyDto):
    print(body)
    return { "data": { "message": "Item created", "item": body } }