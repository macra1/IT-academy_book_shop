from django.urls import path
from crud import views

urlpatterns = [
    # path('create/', views.create, name='create')
    # path('book/', views.read, name='book_read'),
    # path('book/<int:page>', views.read, name='book_read_item'),
    path('book_create/', views.book_create, name='book_create'),
    path('author_create/', views.author_create, name='author_create'),
    path('genre_create/', views.genre_create, name='genre_create'),
    path('publisher_create/', views.publisher_create, name='publisher_create'),
    path('bookview/', views.BookListView.as_view(), name='book_view'),
    path('book_update/<int:book_id>', views.book_update, name='book_update'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('author_update/<int:author_id>', views.author_update, name='author_update'),
    path('author_delete/<int:author_id>', views.author_delete, name='author_delete'),
    path('genre_update/<int:genre_id>', views.genre_update, name='genre_update'),
    path('genre_delete/<int:genre_id>', views.genre_delete, name='genre_delete'),
    path('publisher_update/<int:publisher_id>', views.publisher_update, name='publisher_update'),
    path('publisher_delete/<int:publisher_id>', views.publisher_delete, name='publisher_delete'),
    path('<modeltype>/', views.univread, name='univread'),
    path('<modeltype>/<int:page>', views.univread_detail),
    # path('Author/<int:page>', views.read, name='book_read'),
    # path('Valuta/<int:page>', views.read, name='book_read'),
    # path('Genre/<int:page>', views.read, name='book_read'),
    # path('Publisher/<int:page>', views.read, name='book_read'),
    # path('Series/<int:page>', views.read, name='book_read'),
]