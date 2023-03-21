from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializersTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test_book 1', price=25, author_name='Author 1')
        book_2 = Book.objects.create(name='Test_book 2', price=55, author_name='Author 2')

        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test_book 1',
                'price': '25.00',
                'author_name': 'Author 1',
            },
            {
                'id': book_2.id,
                'name': 'Test_book 2',
                'price': '55.00',
                'author_name': 'Author 2'
            },
        ]
        print(data)
        print(expected_data)
        self.assertEqual(expected_data, data)