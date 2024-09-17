from django.urls import path
from main.views import show_main, create_product

app_name = 'main'

urlpatterns = [
    path('create-product', create_product, name='create_product'),
]