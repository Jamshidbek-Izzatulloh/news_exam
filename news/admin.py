from django.contrib import admin
from .models import NewsCategoryModel,NewsModel,CommentModel

admin.site.register(NewsModel)
admin.site.register(NewsCategoryModel)
admin.site.register(CommentModel)   
# Register your models here.
