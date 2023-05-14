from django.urls import path
from tags import views

urlpatterns = [
    path('/create/', views.CreateTag, name='tag_create'),
]