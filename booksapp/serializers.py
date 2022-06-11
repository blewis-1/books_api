from rest_framework import serializers
from booksapp.models import Book 

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = '__all__'
