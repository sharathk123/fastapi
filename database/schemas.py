def getbook(book):
    if book is None:
        return None  # Handle case where the book is None

    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "pages": book["pages"],
        "genres": book["genres"],
        "rating": book["rating"]
    }


def getbooks(books):
    return [getbook(book) for book in books]
