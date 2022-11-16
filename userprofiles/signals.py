from .models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name
        )


post_save.connect(create_profile, sender=User)
