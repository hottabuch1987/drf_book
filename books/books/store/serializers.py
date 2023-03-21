from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Book, UserBookRelation


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'author_name',)





class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')


