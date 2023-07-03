from django.db import models
from datetime import datetime

class NewsCategoryModel(models.Model):
    name = models.CharField(max_length=100, default='Unknown')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'category'

class NewsModel(models.Model):
    title = models.CharField(max_length=200, default='Title')
    category = models.ForeignKey(NewsCategoryModel, on_delete=models.CASCADE)
    content = models.TextField(default='Not Given')
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'news'

class CommentModel(models.Model):
    author = models.CharField(max_length=50)
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return f"Comment from {self.author} on the news '{self.news}'"
    
    class Meta:
        db_table = 'comment'



