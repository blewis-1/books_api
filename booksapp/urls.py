from booksapp import views
from django.urls import path

urlpatterns = [
    path("books/", views.books_list),
    path('books/<int:id>', views.book_detail,),
]