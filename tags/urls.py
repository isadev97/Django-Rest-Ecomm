from django.urls import path
from tags import views

urlpatterns = [
    path('create/', views.CreateTag.as_view(), name='tag_create'),
]