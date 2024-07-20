
from django.contrib import admin
from django.urls import path
from .views import index, showArticle, profil, add

app_name = 'kwetu'

urlpatterns = [
    path('', index, name='index'),
    path('<int:produit_id>/', showArticle, name='articleId'),
    path('profil/', profil, name='profil'),
    path('add_Product/', add, name='addProduct')
]

