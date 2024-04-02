from django.shortcuts import render, get_object_or_404, redirect
from news.forms import CategoryForm
from news.models import News, Category


def home(request):
    context = {
        'news': News.objects.all()
    }
    return render(request, 'home.html', context)


def news_details(request, id):
    context = {
        'news': get_object_or_404(News, id=id)
    }
    return render(request, 'news_details.html', context)


def categories_form(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
        return redirect('home-page')
    context = {
        'form': form
    }
    return render(request, 'categories_form.html', context)
