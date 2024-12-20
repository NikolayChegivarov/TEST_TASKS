class Book:
    def __init__(self, id: int, title: str, author: str, year: int):
        """Инициализирует объект Book с заданными параметрами:"""
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def change_status(self, new_status: str) -> None:
        """Изменяет статус книги. Проверяет на валидность."""
        if new_status.lower() in ["в наличии", "выдана"]:
            self.status = new_status
        else:
            raise ValueError("Неверный статус")

    def __str__(self):
        """Возвращает строковое представление объекта Book с информацией о книге."""
        return f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nStatus: {self.status}"

    def to_dict(self):
        """Преобразует объект Book в словарь со всеми полями."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }
