from django.contrib import admin
from django.urls import path

from article import views

app_name = 'article'

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add-article/', views.add_article, name="add-article"),
    path('article/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.updateArticle, name="update"),
    path('delete/<int:id>', views.deleteArticle, name="delete"),
    path('comment/<int:id>', views.add_comment, name="comment"),
]