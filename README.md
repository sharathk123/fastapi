# FastAPI CRUD Application with MongoDB

This is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI and MongoDB. The application manages a collection of books, allowing users to create, retrieve, update, and delete book records.

## Features

- Create a new book
- Retrieve all books
- Retrieve a specific book by ID
- Update an existing book by ID
- Delete a book by ID

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **MongoDB**: A NoSQL database for storing book data.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: An ASGI server for running the FastAPI application.

## Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- MongoDB server

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sharathk123/fastapi.git
   cd fastapi

## Usage
1. **Start your MongoDB server** (if it's not already running).

2. **Run the application:**

   uvicorn main:app --reload

   The application will be accessible at http://127.0.0.1:8000.

3. **API Documentation:**

   You can view the API documentation at http://127.0.0.1:8000/docs. 
   This interactive documentation allows you to test the API endpoints directly from your browser.
