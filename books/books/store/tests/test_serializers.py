from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializersTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test_book 1', price=25)
        book_2 = Book.objects.create(name='Test_book 2', price=55)

        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test_book 1',
                'price': '25.00'
            },
            {
                'id': book_2.id,
                'name': 'Test_book 2',
                'price': '55.00'
            },
        ]
        self.assertEqual(expected_data, data)