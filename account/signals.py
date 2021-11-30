from .models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_send_email(sender, instance, created, *args, **kwargs):
    if created:
        
        pass