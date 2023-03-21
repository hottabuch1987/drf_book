from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Book, UserBookRelation, Profile


# Register your models here.
@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass


@admin.register(UserBookRelation)
class UserBookRelationAdmin(ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    pass