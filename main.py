from stats import count_words, count_letters, sort_letters
from typing import Any
import sys


def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()


def print_report(book_count: int, letters: list[dict[str, Any]]):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_count} total words")
    print("--------- Character Count -------")
    for dict in letters:
        print(f"{dict['letter']}: {dict['num']}")
    print("============= END ===============")


def __main__():
    try:
        book_path: str = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text: str = get_book_text(book_path)
    book_count: int = count_words(book_text)
    book_letters: dict[str, int] = count_letters(book_text)
    sorted_letters: list[dict[str, Any]] = sort_letters(book_letters)

    #    print(f"{book_count} words found in the document")
    #    print(book_letters)
    print_report(book_count, sorted_letters)


__main__()
