import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тест 2: Проверка добавления книги второй раз в словарь books_rating
    def test_add_new_book_added_book_name_not_added(self, collector):
        # добавляем уже имеющуюся книгу
        book_name = 'Война и мир'
        collector.add_new_book(book_name)

        # проверяем, что книга не добавилась
        # в обьекте collector три книги
        assert len(collector.get_books_rating()) == 3

    # тест 3: Проверка валидной установки рейтинга: 1, 5, 10 для книги 'Война и мир'
    @pytest.mark.parametrize("rating", [1, 5, 10])
    def test_set_book_rating_valid_rating_1_5_10_added(self, rating, collector):
        book_name = 'Война и мир'
        collector.set_book_rating(book_name, rating)
        assert collector.get_book_rating(book_name) == rating

    # тест 4: Проверка не валидной установки рейтинга: 0, 11
    @pytest.mark.parametrize("rating", [0, 11])
    def test_set_book_rating_not_valid_rating_0_11_not_added(self, rating, collector):
        book_name = 'Война и мир'
        collector.set_book_rating(book_name, rating)
        assert collector.get_book_rating(book_name) != rating

    # тест 5: Проверка получения рейтинга книги по ее имени
    def test_get_book_rating_book_name_rating_received_3(self, collector):
        book_name = 'Война и мир'
        assert collector.get_book_rating(book_name) == 3

    # тест 6: Проверка списка книги 'Book name' с определенным рейтингом: 1, 5, 10
    @pytest.mark.parametrize("rating", [1, 5, 10])
    def test_get_books_with_specific_rating_1_5_10_for_book_name_only_one_book_in_list(self, rating, collector):
        book_name = 'Война и мир'
        collector.set_book_rating(book_name, rating)
        assert len(collector.get_books_with_specific_rating(rating)) == 1

    # тест 7: Проверка получения книг из словаря
    def test_get_books_rating_dictionary_received_book_name_3(self, collector):
        assert len(collector.get_books_rating()) == 3

    # тест 8: Проверяем добавление книги 'Book name' в Избранное
    def test_add_book_in_favorites_book_name_added_in_favorites(self, collector):
        book_name = 'Война и мир'
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1
        assert book_name in collector.get_list_of_favorites_books()

    # тест 9: Проверяем повторное добавление книги 'Book name' в Избранное
    def test_add_book_in_favorites_book_name_added_only_once(self, collector):
        book_name = 'Война и мир'
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    # тест 10: Проверяем удаление книги 'Book name' из Избранного
    def test_delete_book_from_favorites_book_name_deleted(self, collector):
        book_name = 'Война и мир'
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0

    # тест 11: Проверка получения списка Избранных книг
    def test_get_list_of_favorites_books_book_name_received(self, collector):
        book_name_1 = 'Война и мир'
        book_name_2 = 'Дядя Федор, Кот и Пес'
        book_name_3 = 'Задача трех тел'

        collector.add_book_in_favorites(book_name_1)
        collector.add_book_in_favorites(book_name_2)
        collector.add_book_in_favorites(book_name_3)

        favorites = collector.get_list_of_favorites_books()

        assert len(favorites) == 3
        assert book_name_1 in favorites
        assert book_name_2 in favorites
        assert book_name_3 in favorites

