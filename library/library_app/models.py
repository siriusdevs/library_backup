from django.db import models
from django.core.exceptions import ValidationError
from uuid import uuid4


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4) # функцию, а не результат

    class Meta:
        abstract = True

class CreatedMixin(models.Model):
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class ModifiedMixin(models.Model):
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Author(UUIDMixin, CreatedMixin, ModifiedMixin):
    full_name = models.TextField()
    books = models.ManyToManyField('Book', through='BookAuthor')

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'author'

def validate_volume(volume: int):
    if volume <= 0:
        raise ValidationError(   # from django.core.exceptions
            f'Volume {volume} is less or equal zero',
            params={'volume': volume}
        )

# types of goods
type_choices = (
    ('book', 'book'),
    ('magazine', 'magazine')
)

class Book(UUIDMixin, CreatedMixin, ModifiedMixin):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    volume = models.IntegerField(validators=[validate_volume]) # calling validator for volume field
    type = models.CharField(max_length=20, choices=type_choices, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    authors = models.ManyToManyField(Author, through='BookAuthor')
    genres = models.ManyToManyField('Genre', through='BookGenre')

    def __str__(self):
        return f'{self.title}, {self.type} year {self.year}'

    class Meta:
        db_table = 'book'


class BookAuthor(UUIDMixin, CreatedMixin):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'book_author'
        unique_together = (('book', 'author'),)


genre_choices = (
    ('fantasy', 'fantasy'),
    ('fiction', 'fiction'),
    ('detective', 'detective')
)

class Genre(UUIDMixin, CreatedMixin, ModifiedMixin):
    name = models.CharField(choices=genre_choices, max_length=30)
    description = models.TextField(blank=True, null=True)
    books = models.ManyToManyField(Book, through='BookGenre')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genre'


class BookGenre(UUIDMixin, CreatedMixin):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'book_genre'
        unique_together = (('book', 'genre'),)



