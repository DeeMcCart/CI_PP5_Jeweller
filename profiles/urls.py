from django.urls import path
from . import views

urlpatterns = [
    path('<int:profile_id>/', views.profile_detail, name='profile_detail'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),]
