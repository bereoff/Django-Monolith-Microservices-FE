from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from blog.models import Post


def get_permission(user_obj):
    admin_group, created = Group.objects.get_or_create(name="Admin")
    regular_user_group, created = Group.objects.get_or_create(
        name="Regular User")

    content_type = ContentType.objects.get_for_model(Post)
    post_permission = Permission.objects.filter(content_type=content_type)

    for perm in post_permission:
        if perm.codename != "delete_post":
            regular_user_group.permissions.add(perm)

        admin_group.permissions.add(perm)

    if user_obj.is_staff:
        admin_group.user_set.add(user_obj)
    else:
        regular_user_group.user_set.add(user_obj)
