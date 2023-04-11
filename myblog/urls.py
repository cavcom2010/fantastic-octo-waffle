from django.urls import path
from . import views


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path('about/', views.about, name='about'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/<int:pk>/post_delete/', views.post_delete, name='post_delete'),

    
]
