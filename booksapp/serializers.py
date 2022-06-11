from rest_framework import serializers
from booksapp.models import Book 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = '__all__'
