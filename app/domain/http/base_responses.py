BASE_RESPONSES = {
    201: {
        "description": "Created",
        "content": {
            "application/json": {
                "example": {
                    "data": {
                        "message": "Item created successfully",
                        "item": "..."
                    }
                }
            }
        }  
    },
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "example": {
                    "status": 400,
                    "details": [
                        {"message": "…", "type": "validation_error"}
                    ],
                }
            }
        },
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {
                "example": {
                    "status": 500,
                    "details": "Internal Server Error"
                }
            }
        },
    },
}