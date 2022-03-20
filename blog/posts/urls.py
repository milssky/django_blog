from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/category/<slug:slug>/', views.category_list, name='category_list'),
    path('posts/category/<slug:slug>/<int:post_id>/', views.post_detail, name='post_detail'),
]
