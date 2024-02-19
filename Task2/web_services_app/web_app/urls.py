from django.urls import path

from .views import DeletePostView, NewPostView, PostListView

urlpatterns = [
    path("new/", NewPostView.as_view(), name="new_post"),
    path("delete/", DeletePostView.as_view(), name="delete"),
    path("", PostListView.as_view(), name="posts"),

]
