from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

import article
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def dashboard(request):
    articles = Article.objects.all
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)

@login_required(login_url='user:login')
def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        #article.author = request.user
        article.save()
        redirect('article:dashboard')
    return render(request, "add-article.html", {"form": form})

@login_required(login_url='user:login')
def detail(request, id):
    article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id = id)
    return render(request, "detail.html", {"article": article})

@login_required(login_url='user:login')
def updateArticle(request, id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.save()
        
        return redirect('article:dashboard')
    
    return render(request, "update.html", {"form": form})

@login_required(login_url='user:login')
def deleteArticle(request, id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    return redirect('article:dashboard')

def add_comment(request, id):
    article = get_object_or_404(Article, id = id)
    
    if request.method == 'POST':
        comment_content = request.POST.get("comment_content")
        new_comment = Comment(comment_content = comment_content, comment_user = request.user)
        new_comment.article = article
        new_comment.save()
    
    return redirect(f"/article/article/{id}")

