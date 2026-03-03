from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.config.env import env
from app.entrypoints.api.transactions import router as transaction_router

app = FastAPI(
    title=env.app_name,
    swagger_ui_parameters={
        "deepLinking": True,
        "showExtensions": True,
    },
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = exc.errors()
    modified_details = []
    for error in details:
        modified_details.append(
            {
                "error":f"{'.'.join([field for field in error['loc'][1:]])} {error['msg']}",
                "type": error["type"],
            }
        )
    status_code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder({
            "status": status_code,
            "details": modified_details
        }),
    )



app.include_router(router=transaction_router)