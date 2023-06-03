from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from authentication.views import SignUpView

urlpatterns = [
    path('sign_up', SignUpView.as_view(), name='sign_up'),
    path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]