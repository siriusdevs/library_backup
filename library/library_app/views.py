from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Book, Genre, Author


SECRET_URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
PAGINATOR_THRESHOLD = 20

GENRES_CATALOG = 'catalog/genres_page.html'
GENRE_ENTITY = 'entities/genre.html'
BOOKS_CATALOG = 'catalog/books_page.html'
BOOK_ENTITY = 'entities/book.html'


def custom_main(req):
    """Renders request (req) to custom index.html page.
    Args:
        req : http request.
    """
    books = Book.objects.all().count()
    authors = Author.objects.all().count()
    genres = Genre.objects.all().count()

    return render(
        req,
        'index.html',
        context = {
            'books': books,
            'authors': authors,
            'genres': genres
        },
    )


def redirection_page(req):
    """Redirects you elsewhere.
    Args:
        req : http request.
    """
    return redirect(SECRET_URL)


def catalog_view(cls_model, context_name, template):
    class CustomListView(ListView):
        """Generic class-based view listing custom objects."""

        model = cls_model
        template_name = template
        paginate_by = PAGINATOR_THRESHOLD
        context_object_name = context_name

        def get_context_data(self, **kwargs):
            """Passes contest to generic html.
            Args:
                **kwargs: context that we ought to get.
            """
            context = super().get_context_data(**kwargs)
            genres = cls_model.objects.all()
            paginator = Paginator(genres, PAGINATOR_THRESHOLD)
            page_num = self.request.GET.get('page')
            page_obj = paginator.get_page(page_num)
            context[f'{context_name}_list'] = page_obj
            return context

    return CustomListView

def entity_view(cls_model, name, template):
    def view(req):
        """Renders request (req) to custom genre.html page.
        Args:
            req : http request.
        """
        found_id = req.GET.get('id', '')
        found_genre = cls_model.objects.get(id=found_id)

        return render(
            req,
            template,
            context = {
                name: found_genre
            },
        )
    return view

GenreListView = catalog_view(Genre, 'genres', GENRES_CATALOG)
genre = entity_view(Genre, 'genre', GENRE_ENTITY)

BookListView = catalog_view(Book, 'books', BOOKS_CATALOG)
book = entity_view(Book, 'book', BOOK_ENTITY)


