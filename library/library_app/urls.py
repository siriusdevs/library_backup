from django.urls import path
from .views import custom_main, redirection_page, genre, book, GenreListView, BookListView


urlpatterns = [
    path('homepage/', custom_main, name='homepage'),
    path('redirect/', redirection_page, name='redirect'),
    # genres pages
    path('genres/', GenreListView.as_view(), name='genres'),
    path('genre/', genre, name='genre'),
    # books pages
    path('books/', BookListView.as_view(), name='books'),
    path('book/', book, name='book'),
]