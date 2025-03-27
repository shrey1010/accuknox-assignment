from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, Log
import time
import threading

@receiver(post_save, sender=Book)
def book_saved_handler(sender, instance, **kwargs):
    print(f"[Signal] Thread ID: {threading.get_ident()}")
    time.sleep(2)  # Simulate delay to prove sync
    Log.objects.create(message=f"Book '{instance.title}' saved.")