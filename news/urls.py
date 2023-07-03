from django.urls import path
from .views import (AllNewsView,ReadNewsView,CreateNewsView,
                    UpdateNewsView,DeleteNewsView,
                    AllCategoryView,ReadCategoryView,CreateCategoryView,
                    UpdateCategoryVew,DeleteCategoryView)

urlpatterns = [
    #News Views
    path('', AllNewsView.as_view()),
    path('<int:news_id>/', ReadNewsView.as_view()),
    path('create/', CreateNewsView.as_view()),
    path('update/<int:news_id>', UpdateNewsView.as_view()),
    path('delete/<int:news_id>', DeleteNewsView.as_view()),

    #Category Views
    path('categories/', AllCategoryView.as_view()),
    path('categories/<int:category_id>/', ReadCategoryView.as_view()),
    path('categories/create/', CreateCategoryView.as_view()),
    path('categories/update/<int:category_id>/', UpdateCategoryVew.as_view()),
    path('categories/delete/<int:category_id>/', DeleteCategoryView.as_view()),
]