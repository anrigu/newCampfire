from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
	path('books/', views.BooksListCreateAPI.as_view()),
    #Path query example: books/?title=Book1&author=Author&tag=Tag&lower_year=1900&upper_year=2500
    path('authors/', views.AuthorsListCreateAPI.as_view()),
    path('tags/', views.TagsListAPI.as_view()),
    path('tags/create', views.TagsCreateAPI.as_view()),
    #path('books/', views.BooksListCreateAPI.as_view())
    #path('books/', views.BooksListCreateAPI.as_view())
    #path('books/', views.BooksListCreateAPI.as_view())
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
