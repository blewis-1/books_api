from rest_framework.decorators import api_view
from rest_framework.response import Response
from booksapp.models import Book
from booksapp.serializers import BookSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def books_list(request):
    """
    List all books and create a new book.
    """
    if request.method == "GET":
        books = Book.objects.all()
        serialized_books = BookSerializer(books, many=True)
        return Response(serialized_books.data)

    elif request.method == 'POST':    
        serialized_book = BookSerializer(data=request.data)    
        if serialized_book.is_valid():
            serialized_book.save()
            return Response(serialized_book.data,status=status.HTTP_201_CREATED)
        return Response(serialized_book.errors, status=status.HTTP_400_BAD_REQUEST)   


@api_view(['GET','PUT','DELETE'])
def book_detail(request, id):
    """
        Retrive, Update or Delete a book
    """
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        # serialized book
        serialized_book = BookSerializer(book,)
        # return response
        return Response(serialized_book.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serialized_book = BookSerializer(book, data=request.data) 
        if serialized_book.is_valid():
            serialized_book.save()
            return Response(serialized_book.data, status=status.HTTP_200_OK)
        return Response(serialized_book.error , status=status.HTTP_400_BAD_REQUEST)    

    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)