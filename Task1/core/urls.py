
from django.contrib import admin
from django.urls import include, path

from accounts.views import LoginView, RegisterView
from blog.views import NewPostView, PostDelete, PostList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path("new/", NewPostView.as_view(), name="new_post"),
    path("<int:pk>/", PostDelete.as_view(), name="delete"),
    path("", PostList.as_view(), name="index"),
]
