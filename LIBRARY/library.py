import json
from typing import List  # Dict
from book import Book


class Library:
    def __init__(self, filename: str = "data.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        """Загружает список книг из JSON-файла."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            return [
                Book(
                    book_dict['id'],
                    book_dict['title'],
                    book_dict['author'],
                    book_dict['year']
                )
                for book_dict in data
            ]
        except FileNotFoundError:
            return []

    def save_books(self) -> None:
        """Сохраняет текущий список книг в JSON-файл."""
        books_data = [book.to_dict() for book in self.books]
        with open(self.filename, 'w') as file:
            json.dump(books_data, file)

    def add_book(self, title: str, author: str, year: int) -> Book:
        """Добавляет новую книгу в библиотеку и сохраняет изменения."""
        new_id = max(book.id for book in self.books) + 1 if self.books else 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        return new_book

    def delete_book(self, id: int) -> bool:
        """Удалить книгу."""
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                self.save_books()
                return True
        return False

    def search_by_title(self, title: str) -> List[Book]:
        """Ищет книги по части названия."""
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author: str) -> List[Book]:
        """Ищет книги по части имени автора."""
        return [book for book in self.books if author.lower() in book.author.lower()]

    def search_by_year(self, year: int) -> List[Book]:
        """Ищет книги по году выпуска."""
        return [book for book in self.books if book.year == year]

    def display_all_books(self) -> None:
        """Выводит информацию о всех книгах в библиотеке."""
        for book in self.books:
            print(book)
            print("-" * 50)

    def change_status(self, id: int, new_status: str) -> bool:
        """Изменяет статус книги с указанным ID."""
        for book in self.books:
            if book.id == id:
                try:
                    book.change_status(new_status)
                    self.save_books()
                    return True
                except ValueError as e:
                    print(f"Ошибка: {str(e)}")
        return False
