from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('authors', views.author_list, name='author_list'),
    path('<int:author_id>/', views.author_detail, name='author_detail'),
]
