from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView

from .models import Post


class NewPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "new_post.html"
    fields = ["title", "content",]

    def get_success_url(self):
        return reverse("index")


class PostList(ListView):
    model = Post
    template_name = "index.html"
    queryset = Post.objects.all()
    paginate_by = 5


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ("blog.delete_post")
    model = Post
    template_name = "delete.html"

    def get_success_url(self):
        return reverse("index")
