from django import forms
from .models import Category, News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {
            'name': '',
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        labels = {
            'title': 'Título',
            'content': 'Conteúdo',
            'author': 'Autor',
            'image': 'Imagem',
            'categories': 'Categorias'
        }
