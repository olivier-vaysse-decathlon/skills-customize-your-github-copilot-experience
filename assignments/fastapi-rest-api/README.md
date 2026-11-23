# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing books with FastAPI. Practice defining routes, accepting request data, returning JSON responses, and using HTTP status codes.

To run the starter app, install FastAPI and Uvicorn, then start the server:

```bash
pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore and test your API.

## 📝 Tasks

### 🛠️ Read Books

#### Description
Add endpoints that let clients view all books or look up a single book by its ID.

#### Requirements
Completed program should:

- Return all books from `GET /books`.
- Return one book from `GET /books/{book_id}`.
- Return an HTTP 404 response when the requested book does not exist.

### 🛠️ Add Books

#### Description
Create an endpoint that accepts book details as JSON and adds a new book to the collection.

#### Requirements
Completed program should:

- Accept a book title and author in a `POST /books` request body.
- Assign the new book a unique ID.
- Return the created book with HTTP status 201.

### 🛠️ Update and Remove Books

#### Description
Let clients replace a book's details or delete a book by its ID.

#### Requirements
Completed program should:

- Update a book's title and author with `PUT /books/{book_id}`.
- Delete a book with `DELETE /books/{book_id}` and return HTTP status 204.
- Return HTTP 404 when an update or delete targets a book that does not exist.
- Preserve the book's ID when updating it.
