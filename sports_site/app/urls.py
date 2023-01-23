from django.contrib import admin
from django.urls import path, include
# from . import views
from .views import HomeView, ArticleDetailView, DeleteArticleView, AddArticleView, UpdateArticleView, AddPodcastView, DeletePodcastView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('new-article/', AddArticleView.as_view(), name='new-article'),
    path('article/edit/<int:pk>', UpdateArticleView.as_view(), name='update-article'),
    path('article/delete/<int:pk>', DeleteArticleView.as_view(), name='delete-article'),
    path('new-podcast/', AddPodcastView.as_view(), name='new-podcast'),
    path('podcast/delete/<int:pk>', DeletePodcastView.as_view(), name='delete-podcast'),
]