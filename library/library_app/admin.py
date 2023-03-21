from django.contrib import admin
from .models import Genre, Book, Author


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Register Genre Admin Model."""

    model = Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Register Book Admin Model."""
    
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Register Author Admin Model."""
    
    model = Author
