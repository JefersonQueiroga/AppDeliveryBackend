from django.urls import path
from .viewssets import *

urlpatterns = [
    path("login/", LoginViewSet.as_view(), name="login"),
    path("register/", RegisterViewSet.as_view(), name="register"),
]