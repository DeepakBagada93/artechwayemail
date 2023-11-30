from django.urls import path
from . import views

app_name = 'emailapp'

urlpatterns = [
    path('', views.index, name='index'),
]
