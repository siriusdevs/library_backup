from django.db import models


class Author(models.Model):
    id = models.UUIDField(primary_key=True)
    full_name = models.TextField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'author'


class Book(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    volume = models.IntegerField()
    type = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}, {self.type} year {self.year}'

    class Meta:
        db_table = 'book'


class BookAuthor(models.Model):
    id = models.UUIDField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'book_author'
        unique_together = (('book', 'author'),)


class Genre(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'genre'


class BookGenre(models.Model):
    id = models.UUIDField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'book_genre'
        unique_together = (('book', 'genre'),)



