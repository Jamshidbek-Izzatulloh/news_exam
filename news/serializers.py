from rest_framework import serializers
from .models import NewsModel,NewsCategoryModel,CommentModel


class NewsSerializer(serializers.Serializer):
    class Meta:
        model = NewsModel
        fields = '__all__'


class NewsCategorySerializer(serializers.Serializer):
    class Meta:
        model = NewsCategoryModel
        fields = '__all__'

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = CommentModel
        fields = '__all__'

