from django.urls import path, include

from . import views
from .views import basket_add, basket_remove

app_name = 'storeProducts'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/category/<int:category_id>/', views.products, name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add' ),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove' )
]