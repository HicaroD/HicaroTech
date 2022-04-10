from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageListView.as_view(), name="homepage"),
]
