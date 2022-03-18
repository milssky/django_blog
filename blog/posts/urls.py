from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_list, name='category_list')
]
