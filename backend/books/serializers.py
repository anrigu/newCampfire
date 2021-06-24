from rest_framework import serializers
from books import models

class BookSerializer(serializers.ModelSerializer):
    '''Model Serializer automatically creates create and update functions, so 
    unless you need custom versions of these, you don't need to define them here. The create and update functions 
    are automatically called when the view calls serializer.save()'''
    class Meta:
        model = models.Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'    
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'