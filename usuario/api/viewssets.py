from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import *

class LoginViewSet(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterViewSet(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)

class EnderecoCreateViewSet(generics.CreateAPIView):
    serializer_class =EnderecoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.data["user"]= request.user.pk
        return self.create(request, *args, **kwargs)

class EnderecoListViewSet(generics.ListAPIView):
    serializer_class = EnderecoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = Endereco.objects.filter(user = self.request.user)
        return queryset