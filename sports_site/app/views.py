from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm, EditArticleForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles.html'

class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class UpdateArticleView(UpdateView):
    model = Article
    template_name = 'edit_article.html'
    # fields = ['title', 'title_tag', 'body']
    form_class = EditArticleForm

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')