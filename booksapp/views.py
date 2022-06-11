from rest_framework.decorators import api_view
from rest_framework.response import Response
from booksapp.models import Book
from booksapp.serializers import BookSerializers
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def books_list(request):
    """
    List all books and create a new book.
    """
    if request.method == "GET":
        books = Book.objects.all()
        serialized_books = BookSerializers(books, many=True)
        return Response(serialized_books.data)

    elif request.method == 'POST':    
        serialized_book = BookSerializers(data=request.data)    
        if serialized_book.is_valid():
            serialized_book.save()
            return Response(serialized_book.data,status=status.HTTP_201_CREATED)
        return Response(serialized_book.errors, status=status.HTTP_400_BAD_REQUEST)   


@api_view(['GET','PUT','DELETE'])
def book_detail(request, id):
    pass