from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('maint/', views.maint_products, name='maint_products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_confirm/<int:product_id>/', views.delete_confirm, name='delete_confirm'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('review/<int:product_id>/', views.review, name='review'),
]