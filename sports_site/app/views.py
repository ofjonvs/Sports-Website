from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Podcast
from .forms import ArticleForm, EditArticleForm, PodcastForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    ordering = ['-article_date']
    def get(self, request):
        podcasts = Podcast.objects.all()
        articles = Article.objects.all()
        return render(request, 'home.html', {'podcasts': podcasts[:3], 'articles': articles[:5]})

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles.html'

class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class AddPodcastView(CreateView):
    model = Podcast
    form_class = PodcastForm
    template_name = 'add_podcast.html'

class UpdateArticleView(UpdateView):
    model = Article
    template_name = 'edit_article.html'
    # fields = ['title', 'title_tag', 'body']
    form_class = EditArticleForm

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')

class DeletePodcastView(DeleteView):
    model = Podcast
    template_name = 'delete_podcast.html'
    success_url = reverse_lazy('home')