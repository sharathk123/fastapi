from typing import List, Optional

from pydantic import BaseModel, Field


class Book(BaseModel):
    id: str
    title: str
    author: str
    pages: int
    genres: List[str]
    rating: int

    class Config:
        schema_extra = {
            "example": {
                "title": "American Gods",
                "author": "Neil Gaiman",
                "pages": 460,
                "genres": ["fantasy", "mythology"],
                "rating": 8
            }
        }
