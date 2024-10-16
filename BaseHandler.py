from fastapi import HTTPException, status


class BaseHandler:
    """Centralized handler for HTTPExceptions and success responses."""

    @staticmethod
    def handle_exception(e):
        """Handle general exceptions and raise HTTP 500 Internal Server Error."""
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Internal server error: {str(e)}")

    @staticmethod
    def not_found(detail: str = "Resource not found"):
        """Raise HTTP 404 Not Found error."""
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    @staticmethod
    def invalid_id_format(detail: str = "Invalid ID format"):
        """Raise HTTP 400 Bad Request for invalid ObjectId format."""
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

    @staticmethod
    def validation_error(detail: str = "Validation failed"):
        """Raise HTTP 422 Unprocessable Entity for validation errors."""
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)

    @staticmethod
    def success(detail: str = "Success", data: dict = None):
        """Return HTTP 200 OK success message."""
        return {"status_code": status.HTTP_200_OK, "message": detail, "data": data}

    @staticmethod
    def created(detail: str = "Resource created successfully", resource_id: str = None):
        """Return HTTP 201 Created message."""
        return {"status_code": status.HTTP_201_CREATED, "message": detail, "id": resource_id}
