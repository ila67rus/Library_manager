import json
import os
from typing import List, Dict, Any

LIBRARY_FILE = "library.json"


def load_library() -> List[Dict[str, Any]]:
    """Загружает данные библиотеки из файла."""
    if not os.path.exists(LIBRARY_FILE):
        return []
    with open(LIBRARY_FILE, "r") as file:
        return json.load(file)


def save_library(library: List[Dict[str, Any]]) -> None:
    """Сохраняет данные библиотеки в файл."""
    with open(LIBRARY_FILE, "w",encoding='utf-8') as file:
        json.dump(library, file, indent=4,ensure_ascii=False)


def generate_id(library: List[Dict[str, Any]]) -> int:
    """Генерирует уникальный ID для книги."""
    return max((book["id"] for book in library), default=0) + 1


def add_book(library: List[Dict[str, Any]]) -> None:
    """Добавляет книгу в библиотеку."""
    title: str = input("Введите название книги: ").strip()
    author: str = input("Введите автора книги: ").strip()
    year: str = input("Введите год издания: ").strip()

    if not year.isdigit():
        print("Ошибка: Год издания должен быть числом.")
        return

    new_book: Dict[str, Any] = {
        "id": generate_id(library),
        "title": title,
        "author": author,
        "year": int(year),
        "status": "в наличии"
    }
    library.append(new_book)
    save_library(library)
    print("Книга успешно добавлена!")


def delete_book(library: List[Dict[str, Any]]) -> None:
    """Удаляет книгу по ID."""
    try:
        book_id: int = int(input("Введите ID книги для удаления: ").strip())
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return

    for book in library:
        if book["id"] == book_id:
            library.remove(book)
            save_library(library)
            print("Книга успешно удалена!")
            return

    print("Ошибка: Книга с таким ID не найдена.")


def search_book(library: List[Dict[str, Any]]) -> None:
    """Ищет книги по title, author или year."""
    query: str = input("Введите название, автора или год издания для поиска: ").strip()
    results: List[Dict[str, Any]] = [
        book for book in library
        if query.lower() in book["title"].lower()
        or query.lower() in book["author"].lower()
        or query == str(book["year"])
    ]

    if results:
        print("Найденные книги:")
        for book in results:
            print_book(book)
    else:
        print("Книги по вашему запросу не найдены.")


def display_books(library: List[Dict[str, Any]]) -> None:
    """Выводит все книги."""
    if library:
        print("Список всех книг:")
        for book in library:
            print_book(book)
    else:
        print("Библиотека пуста.")


def update_status(library: List[Dict[str, Any]]) -> None:
    """Изменяет статус книги."""
    try:
        book_id: int = int(input("Введите ID книги: ").strip())
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return

    new_status: str = input("Введите новый статус книги ('в наличии' или 'выдана'): ").strip()
    if new_status not in ["в наличии", "выдана"]:
        print("Ошибка: Неверный статус. Используйте 'в наличии' или 'выдана'.")
        return

    for book in library:
        if book["id"] == book_id:
            book["status"] = new_status
            save_library(library)
            print("Статус книги успешно обновлен!")
            return

    print("Ошибка: Книга с таким ID не найдена.")


def print_book(book: Dict[str, Any]) -> None:
    """Выводит информацию о книге."""
    print(f"[ID: {book['id']}] {book['title']} | {book['author']} | {book['year']} | Статус: {book['status']}")


def main() -> None:
    """Главная функция."""
    library: List[Dict[str, Any]] = load_library()
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice: str = input("Выберите действие (1-6): ").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            delete_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            update_status(library)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
