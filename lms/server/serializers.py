from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book, Record, Request


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'cover', 'title', 'summary', 'author', 'published_on')


class RecordSerializer(serializers.ModelSerializer):
    fine = serializers.ReadOnlyField()
    class Meta:
        model = Record
        fields = ('id', 'reader', 'book', 'issue_date', 'return_date', 'fine')


class RequestSerializer(serializers.ModelSerializer):
    reader = serializers.ReadOnlyField(source='reader.username')
    class Meta:
        model = Request
        fields = ('id', 'reader', 'book', 'status')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')
