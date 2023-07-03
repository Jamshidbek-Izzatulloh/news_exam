from django.shortcuts import render, get_object_or_404
from .models import NewsModel, NewsCategoryModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NewsCategorySerializer, NewsSerializer
from rest_framework import status

#News CRUD
class AllNewsView(APIView):
    def get(self,request,*args,**kwargs):
        alldata = NewsModel.objects.all()
        serializer = NewsSerializer(alldata, many=True)
        return Response(serializer.data)
 
class ReadNewsView(APIView):
    def get(self,request,*args,**kwargs):
        data = get_object_or_404(NewsModel, pk=kwargs['news_id'])
        serializer = NewsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateNewsView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateNewsView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(NewsModel, pk=kwargs['news_id'])
        serializer = NewsSerializer(instance, data=request.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
class DeleteNewsView(APIView):
    def delete(self,request,*args,**kwargs):
        instance = get_object_or_404(NewsModel, pk=kwargs['news_id'])
        instance.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

# NewsCategory CRUD
class AllCategoryView(APIView):
    def get(self,request,*args,**kwargs):
        allcateg = NewsCategoryModel.objects.all()
        serializer = NewsCategorySerializer(allcateg)
        return Response(serializer.data)
    
class ReadCategoryView(APIView):
    def get(self,request,*args,**kwargs):
        data = get_object_or_404(NewsCategoryModel, pk=kwargs['category_id'])
        serializer = NewsCategorySerializer(data)
        return Response(serializer.data)

class CreateCategoryView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = NewsCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateCategoryVew(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(NewsCategoryModel, pk=kwargs['category_id'])
        serializer = NewsCategorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteCategoryView(APIView):
    def delete(self,request,*args,**kwargs):
        instance = get_object_or_404(NewsCategoryModel, pk=kwargs['category_id'])
        instance.delete()
        return Response({'message': 'Deleted successfully'})

# -----
class GetCategoryView():
    def get(self,request,*args,**kwargs):
        news = get_object_or_404(NewsModel, pk=kwargs['category_id'])
        serializer = NewsSerializer(news)
        return Response(serializer.data)
    