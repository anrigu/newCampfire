from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #description = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + self.last_name


class Tag(models.Model):
    name = models.CharField(max_length=150)
    #category = models.ForeignKey()

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishing_year = models.IntegerField(default=2500) #Default is the year 2500
    #If author is a foreign key, we can link together books written by the same author 
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

