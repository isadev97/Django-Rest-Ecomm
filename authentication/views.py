from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.serializers import CreateUserSerializer
from rest_framework import status

class SignUpView(APIView):

    def post(self, request):
        create_serializer = CreateUserSerializer(data=request.data)
        if create_serializer.is_valid():
            username = create_serializer.validated_data.get('username')
            email = create_serializer.validated_data.get('email')
            password = create_serializer.validated_data.get('password')
            if User.objects.filter(username=username).exists():
                return Response({"error": True, "error_msg": "Username already taken"})
            if User.objects.filter(email=email).exists():
                return Response({"error": True, "error_msg": "Email already taken"})
            user = User.objects.create_user(username=username, email=email, password=password)
            return Response({"success" : True, "success_msg" : "Try login back with same credentials"})
        else:
            return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)      