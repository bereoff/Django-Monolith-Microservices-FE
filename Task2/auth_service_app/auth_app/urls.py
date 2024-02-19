
from django.urls import path

from .views import ListUsersView, LoginUserView, SignUpUserView

urlpatterns = [
    path("", ListUsersView.as_view(), name="users"),
    path("new/", SignUpUserView.as_view(), name="new_user"),
    path("login/", LoginUserView.as_view(), name="login"),

]
