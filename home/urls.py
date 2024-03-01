from django.urls import path
from . import views
from .views import index

urlpatterns = [path('', index, name='home'),
               path('about', views.about, name='about'), ]
