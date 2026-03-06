from django.urls import path
from . import views

urlpatterns = [
    # Для URL с .html
    path('group_list.html', views.group, name='group'),
    path('index.html', views.index, name='index')
]