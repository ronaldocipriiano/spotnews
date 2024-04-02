from rest_framework import serializers
from news.models import Category, News, User


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'content',
            'author',
            'created_at',
            'image',
            'categories'
        ]
