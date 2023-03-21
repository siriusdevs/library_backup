from django.contrib import admin
from .models import Genre, Book, Author, BookAuthor, BookGenre

class BookAuthor_inline(admin.TabularInline):
    model = BookAuthor
    extra = 1

class BookGenre_inline(admin.TabularInline):
    model = BookGenre
    extra = 1

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Register Genre Admin Model."""

    model = Genre
    inlines = (BookGenre_inline,)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Register Book Admin Model."""
    
    model = Book
    inlines = (BookAuthor_inline, BookGenre_inline) # adding inline to book admin model

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Register Author Admin Model."""
    
    model = Author
    inlines = (BookAuthor_inline,)