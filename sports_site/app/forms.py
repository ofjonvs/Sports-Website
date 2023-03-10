from django import forms
from .models import Article, Podcast

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'title_tag', 'author', 'body', 'snippet', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auth', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}), 
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),           
        }

class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'title_tag', 'body', 'snippet', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),                       
        }

class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full YouTube URL'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
