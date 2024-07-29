from django.urls import path
from .import views#(.)current directory of the file

urlpatterns = [
    path('base/',views.base,name="base"),
    path('bloglist/',views.bloglist,name="bloglist"),
    path('create_blog/',views.create_blog,name="blogcreate"),
]