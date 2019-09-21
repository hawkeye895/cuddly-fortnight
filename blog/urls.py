from django.urls import path
from blog import views


app_name='blog'
urlpatterns = [
    path("blog/", views.blog_index, name="blog_index"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("blog/<category>/", views.blog_category, name="blog_category"),
]