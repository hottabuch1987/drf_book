from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Book, UserBookRelation
from store.serializers import BookSerializer


class BookSerializersTestCase(TestCase):
    def test_ok(self):
        user1 = User.objects.create(username='user1')       ###создаем user
        user2 = User.objects.create(username='user2')
        user3 = User.objects.create(username='user3')

        book_1 = Book.objects.create(name='Test_book 1', price=25, author_name='Author 1') #cоздаеь книги
        book_2 = Book.objects.create(name='Test_book 2', price=55, author_name='Author 2')

        UserBookRelation.objects.create(user=user1, book=book_1, like=True)  #like для 1 книги
        UserBookRelation.objects.create(user=user2, book=book_1, like=True)
        UserBookRelation.objects.create(user=user3, book=book_1, like=True)

        UserBookRelation.objects.create(user=user1, book=book_2, like=True)  #like для 2 книги
        UserBookRelation.objects.create(user=user2, book=book_2, like=True)
        UserBookRelation.objects.create(user=user3, book=book_2, like=False)

        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test_book 1',
                'price': '25.00',
                'author_name': 'Author 1',
                'likes_count': 3
            },
            {
                'id': book_2.id,
                'name': 'Test_book 2',
                'price': '55.00',
                'author_name': 'Author 2',
                'likes_count': 2
            },
        ]
        print(data)
        print(expected_data)
        self.assertEqual(expected_data, data)