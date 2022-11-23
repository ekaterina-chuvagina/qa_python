import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book('Война и мир')
    collector.add_new_book('Дядя Федор, Кот и Пес')
    collector.add_new_book('Задача трех тел')

    collector.set_book_rating('Война и мир', 3)
    collector.set_book_rating('Дядя Федор, Кот и Пес', 3)
    collector.set_book_rating('Задача трех тел', 3)
    return collector
