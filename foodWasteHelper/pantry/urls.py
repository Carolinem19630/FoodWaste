from django.urls import path
from . import views

app_name = 'pantry'

urlpatterns = [
    path("", views.index, name='index'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove'),
    path('email', views.email, name='email')
]