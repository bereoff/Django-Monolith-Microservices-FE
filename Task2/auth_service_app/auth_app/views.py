import json

from django.shortcuts import get_object_or_404
from rest_framework import generics, response, status, views
from rest_framework.authtoken.models import Token

from .models import CustomUser
from .serializers import UsersSerializer


class ListUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer


class LoginUserView(views.APIView):
    def post(self, request):
        user = get_object_or_404(CustomUser, email=request.data["email"])
        if not user.check_password(request.data["password"]):
            return response.Response(
                {"Detail:": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return response.Response({"Token:": token.key})


class SignUpUserView(views.APIView):
    def post(self, request):

        data = json.loads(request.body)
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = CustomUser.objects.get(email=request.data["email"])
            user.set_password(request.data["password"])
            user.save()
            token = Token.objects.create(user=user)
            return response.Response(
                {"user": serializer.data["email"], "Token": token.key}
            )

        return response.Response(
            serializer.errors, status.HTTP_400_BAD_REQUEST)
