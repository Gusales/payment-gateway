from typing import Annotated

from fastapi import Header, HTTPException

def validate_x_idempotency_key(idempotency_key: Annotated[str, Header()]):
    if not idempotency_key:
        raise HTTPException(
            status_code=400,
            detail="Idempotency-Key header not informed"
        )