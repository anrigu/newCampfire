from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from books.serializers import BookSerializer, AuthorSerializer, TagSerializer
from books.models import Book, Author, Tag
from rest_framework.permissions import IsAdminUser
from django.db.models import Q

# Create your views here.
class BooksListCreateAPI(generics.ListCreateAPIView):
    #permission_classes = (IsAdminUser)
    def get_queryset(self):
        """
        Optionally restricts the returned books based on a tag and whether it's included
        """
        queryset = Book.objects.all()
        tagQuery = self.request.query_params.get('tag') #Tag query comes in as a comma separated list
        authorQuery = self.request.query_params.get('author')
        publishingQueryLower = self.request.query_params.get('lower_year')
        publishingQueryUpper = self.request.query_params.get('upper_year')
        titleQuery = self.request.query_params.get('title')
        if titleQuery is not None:
            queryset = queryset.filter(title__icontains = titleQuery)
        if tagQuery is not None:
            tagQuery = tagQuery.split(",")
            for tag in tagQuery:
                queryset = queryset.filter(tags__name__iexact = tag)
            print(queryset)
        if authorQuery is not None:
            queryset = queryset.filter(Q(author__first_name__icontains = authorQuery) | Q(author__last_name__icontains = authorQuery)) # If authorQuery is first name or last name
        if publishingQueryLower is not None:
            queryset = queryset.filter(publishing_year__gte = publishingQueryLower)
        if publishingQueryUpper is not None:
            queryset = queryset.filter(publishing_year__lte = publishingQueryUpper)
        return queryset
    
    serializer_class = BookSerializer

class AuthorsListCreateAPI(generics.ListCreateAPIView):
    #permission_classes = (IsAdminUser)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class TagsListAPI(generics.ListAPIView):
    #permission_classes = (IsAdminUser)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagsCreateAPI(generics.ListCreateAPIView):
    #permission_classes = (IsAdminUser)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class BooksUpdate(generics.RetrieveUpdateAPIView):
    # Retrieve or update a book
    permission_classes = (IsAdminUser)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorsUpdate(generics.RetrieveUpdateAPIView):
    # Retrieve or update a book
    permission_classes = (IsAdminUser)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class TagsUpdate(generics.RetrieveUpdateAPIView):
    # Retrieve or update a book
    permission_classes = (IsAdminUser)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
