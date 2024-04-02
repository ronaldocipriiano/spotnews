from django.urls import path, include
from rest_framework import routers
from news.views import (
    home,
    news_details,
    categories_form,
    news_form,
    CategoryViewSet,
    UserViewSet,
)


router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', home, name='home-page'),
    path('news/<int:id>', news_details, name='news-details-page'),
    path('categories', categories_form, name='categories-form'),
    path('news', news_form, name='news-form'),
    path('api/', include('news.urls')),
]

urlpatterns += router.urls
