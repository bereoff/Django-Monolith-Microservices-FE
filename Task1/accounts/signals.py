
from django.db.models.signals import post_save

from .models import CustomUser
from .permissions import get_permission


def adding_user_to_a_group(sender, instance, created, **kwargs):

    if created:
        get_permission(user_obj=instance)


post_save.connect(adding_user_to_a_group, sender=CustomUser)
