from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    # author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    author = models.CharField(max_length=30, blank=True, default="John Doe")
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='article_img', blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # approve = models.chec
    
    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment")
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.comment_user}-{self.comment_date}"