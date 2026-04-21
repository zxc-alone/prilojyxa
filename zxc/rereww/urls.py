from django.urls import path, include
from . import views

app_name = 'rereww'

urlpatterns = [
    path('', views.index, name='index'),
    path('group_list/', views.group_list, name='group_list'),
    path('group/<slug:slug>/', views.group, name='group'),
    path('index.html', views.index, name='index'),
    path('group_list.html', views.group_list, name='group_list'),
]