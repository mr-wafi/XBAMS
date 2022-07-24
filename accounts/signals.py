from django.db.models.signals import post_save
from django.contrib.auth.models import User
from.models import Account
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=Account)
def build_profile_on_user_creation(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.save()