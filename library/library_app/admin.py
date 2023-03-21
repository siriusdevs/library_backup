from django.contrib import admin
from .models import Genre, Book, Author, BookAuthor, BookGenre, genre_choices


# class DecadeBornListFilter(admin.SimpleListFilter): # TODO filter by genre
#     title = 'Genre'

#     parameter_name = 'genre'

#     def lookups(self, request, model_admin):
#         genres = [item[0] for item in genre_choices]
#         return [(genre, genre) for genre in genres]

#     def queryset(self, request, queryset):
#         if self.value() == '80s':
#             return queryset.filter(
#                 genre_=date(1980, 1, 1),
#                 birthday__lte=date(1989, 12, 31),
#             )
#         if self.value() == '90s':
#             return queryset.filter(
#                 birthday__gte=date(1990, 1, 1),
#                 birthday__lte=date(1999, 12, 31),
#             )

# class PersonAdmin(admin.ModelAdmin):
#     list_filter = (DecadeBornListFilter,)

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
    list_filter = (
        'name',
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Register Book Admin Model."""
    
    model = Book
    inlines = (BookAuthor_inline, BookGenre_inline) # adding inline to book admin model
    list_filter = (
        'title',
        'year',
        'volume',
        'type',
        'created'
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Register Author Admin Model."""
    
    model = Author
    inlines = (BookAuthor_inline,)
    list_filter = (
        'full_name',
    )