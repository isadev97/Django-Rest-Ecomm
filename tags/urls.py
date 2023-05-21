from django.urls import path
from tags import views

urlpatterns = [
    path('create/', views.CreateTag.as_view(), name='tag_create'),
    path('list/v1/', views.ListTagV1.as_view(), name='tag_list_v1'),
    path('list/v2/', views.ListTagV2.as_view(), name='tag_list_v2'),
    path('detail/<str:slug>/', views.TagDetailV1.as_view(), name='tag_details_v1'),
    path('detail/v2/<str:slug>/', views.TagDetailV2.as_view(), name='tag_details_v2'),
]