from django.urls import path
from crud import views

urlpatterns = [
    # path('create/', views.create, name='create')
    # path('book/', views.read, name='book_read'),
    # path('book/<int:page>', views.read, name='book_read_item'),
    path('book_create/', views.book_create, name='book_create'),
    path('bookview/', views.BookListView.as_view(), name='book_view'),
    path('book_update/<int:book_id>', views.book_update, name='book_update'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('<modeltype>/', views.univread, name='univread'),
    path('<modeltype>/<int:page>', views.univread_detail),
    # path('Author/<int:page>', views.read, name='book_read'),
    # path('Valuta/<int:page>', views.read, name='book_read'),
    # path('Genre/<int:page>', views.read, name='book_read'),
    # path('Publisher/<int:page>', views.read, name='book_read'),
    # path('Series/<int:page>', views.read, name='book_read'),
]