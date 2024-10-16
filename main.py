from bson import ObjectId
from fastapi import APIRouter, FastAPI

from BaseHandler import BaseHandler

from database.models import Book
from configuration import collection
from database.schemas import getbooks, getbook

app = FastAPI()
router = APIRouter()


# Create a new book
@router.post("/books", summary="Create a new book")
async def create_book(book: Book):
    """
    Create a new book.

    Args:
        book: The details of the book to create.

    Returns:
        A message indicating the success of the creation along with the new book's ID.
    """
    try:
        resp = collection.insert_one(dict(book))
        return BaseHandler.created("Book created successfully.", resource_id=str(resp.inserted_id))
    except Exception as e:
        raise BaseHandler.handle_exception(e)


# Retrieve all books
@router.get("/books", summary="Retrieve all books")
async def get_all_books():
    """
    Retrieve all books.

    Returns:
        A list of all books.
    """
    try:
        data = collection.find()
        return BaseHandler.success("Books retrieved successfully.", data=getbooks(data))
    except Exception as e:
        raise BaseHandler.handle_exception(e)


# Retrieve a specific book by ID
@router.get("/books/{id}", summary="Get a specific book by ID")
async def get_book(id: str):
    """
    Retrieve a book by its ID.

    Args:
        id: The ID of the book to retrieve.

    Returns:
        The requested book details.
    """
    try:
        book_id = ObjectId(id)  # Convert to ObjectId
        data = collection.find_one({"_id": book_id})

        if not data:
            raise BaseHandler.not_found("Book not found")

        return BaseHandler.success("Book retrieved successfully.", data=getbook(data))
    except ValueError:
        raise BaseHandler.invalid_id_format()
    except Exception as e:
        raise BaseHandler.handle_exception(e)


# Update an existing book by ID
@router.put("/books/{id}", summary="Update an existing book by ID")
async def update_book(id: str, book: Book):
    """
    Update an existing book by its ID.

    Args:
        id: The ID of the book to update.
        book: The new details of the book.

    Returns:
        A message indicating the success of the update.
    """
    try:
        book_id = ObjectId(id)  # Convert to ObjectId
        update_data = book.dict(exclude_unset=True)  # Only update fields that are set

        result = collection.update_one({"_id": book_id}, {"$set": update_data})

        if result.modified_count == 0:
            raise BaseHandler.not_found("Book not found or no changes made")

        return BaseHandler.success("Book updated successfully.")
    except ValueError:
        raise BaseHandler.invalid_id_format()
    except Exception as e:
        raise BaseHandler.handle_exception(e)


# Delete a specific book by ID
@router.delete("/books/{id}", summary="Delete a book by ID")
async def delete_book(id: str):
    """
    Delete a book by its ID.

    Args:
        id: The ID of the book to delete.

    Returns:
        A message indicating the success of the deletion.
    """
    try:
        book_id = ObjectId(id)  # Convert to ObjectId

        # Attempt to delete the book
        result = collection.delete_one({"_id": book_id})

        if result.deleted_count == 0:
            raise BaseHandler.not_found("Book not found")

        return BaseHandler.success("Book deleted successfully.")
    except ValueError:
        raise BaseHandler.invalid_id_format()
    except Exception as e:
        raise BaseHandler.handle_exception(e)

app.include_router(router)