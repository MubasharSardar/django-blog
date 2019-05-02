from django.views.generic import ListView, DetailView
from django.conf.urls import url
from django.urls import path
from .models import post


# url pattern for displaying post in list as well in detail
urlpatterns = [
    url(r'^$',ListView.as_view(queryset=post.objects.all().order_by("-date")[:25],template_name="blog/index.html")),
    url(r'(?P<pk>\d+)$',DetailView.as_view(model=post, template_name="blog/post.html")),
]


