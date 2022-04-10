from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from articles.models import Article

class HomepageListView(ListView):
    model = Article
    template_name = "homepage.html"
