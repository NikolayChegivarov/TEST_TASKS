from library import Library
from utils import get_user_input, get_int_input, yes_no_question


def main():
    """
    Основная функция программы. Обеспечивает взаимодействие пользователя с системой управления библиотекой.

    Пример использования:
    main() - Запускает главный цикл программы и позволяет пользователю выполнять различные действия с библиотекой.
    """

    library = Library()
    """
    Создает экземпляр класса Library для управления библиотекой.
    """

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        try:
            choice = get_int_input("Выберите действие: ")
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        if choice == 1:
            title = get_user_input("Введите название книги: ")
            author = get_user_input("Введите автора книги: ")
            year = get_int_input("Введите год издания: ")
            new_book = library.add_book(title, author, year)
            print(f"\nКнига добавлена:\n{new_book}")

        elif choice == 2:
            id_to_delete = get_int_input("Введите ID книги для удаления: ")
            if library.delete_book(id_to_delete):
                print("Книга удалена успешно.")
            else:
                print("Книга с таким ID не найдена.")

        elif choice == 3:
            print("\nВыберите критерий поиска:")
            print("1. По названию")
            print("2. По автору")
            print("3. По году издания")

            try:
                search_choice = get_int_input("Введите номер выбора: ")
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue

            if search_choice not in range(1, 4):
                print("Неверный выбор. Попробуйте еще раз.")
                continue

            if search_choice == 1:
                title = get_user_input("Введите название книги: ")
                results = library.search_by_title(title)
            elif search_choice == 2:
                author = get_user_input("Введите автора книги: ")
                results = library.search_by_author(author)
            elif search_choice == 3:
                year = get_int_input("Введите год издания: ")
                results = library.search_by_year(year)

            if results:
                print(f"\nРезультаты поиска ({len(results)} книг):")
                for book in results:
                    print(book)
                    print("-" * 50)
            else:
                print("Совпадений не найдено.")

        elif choice == 4:
            library.display_all_books()

        elif choice == 5:
            id_to_change = get_int_input("Введите ID книги для изменения статуса: ")
            new_status = get_user_input("Введите новый статус ('в наличии' или 'выдана'): ").lower()
            if library.change_status(id_to_change, new_status):
                print("Статус изменен успешно.")
            else:
                print("Книга с таким ID не найдена.")

        elif choice == 6:
            if yes_no_question("Вы уверены, что хотите выйти? (да/нет): "):
                break
            else:
                print("Продолжаем работу.")


if __name__ == "__main__":
    main()
