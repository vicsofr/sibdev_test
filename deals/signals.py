from django.core.cache import cache
from django.db.models.signals import post_init
from django.dispatch import receiver

from .models import Deal


@receiver(post_init, sender=Deal, dispatch_uid='post_init')
def object_post_init_handler(sender, **kwargs):
    cache.delete('top_clients')
