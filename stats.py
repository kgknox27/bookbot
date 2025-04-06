from typing import Any


def count_words(book: str):
    book_array = book.split()
    count: int = len(book_array)

    return count


def count_letters(book: str):
    letters_count: dict[str, int] = {}

    for char in book:
        lowered = char.lower()
        if lowered not in letters_count:
            letters_count[lowered] = 1
        else:
            letters_count[lowered] += 1

    return letters_count


def sort_on(dict: dict[str, Any]):
    return dict["num"]


def sort_letters(letters_count: dict[str, int]):
    sorted_letters: list[dict[str, Any]] = []

    for key in letters_count:
        if key.isalpha():
            sorted_letters.append({"letter": key, "num": letters_count[key]})

    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters
