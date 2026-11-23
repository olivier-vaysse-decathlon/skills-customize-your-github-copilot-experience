from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Books API')


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title='The Hobbit', author='J.R.R. Tolkien'),
    2: Book(id=2, title='A Wrinkle in Time', author="Madeleine L'Engle"),
}
next_book_id = 3

# Add your GET, POST, PUT, and DELETE endpoints below.
