from django.test import TestCase
from django.db import transaction
from .models import Book, Log
import threading
import time

class SignalTests(TestCase):
    def test_sync_execution(self):
        start = time.time()
        Book.objects.create(title="Test Book")
        end = time.time()
        print(f"Total Time: {end - start:.2f} seconds")

    def test_same_thread(self):
        print(f"[Caller] Thread ID: {threading.get_ident()}")
        Book.objects.create(title="Thread Check")

    def test_transaction_scope(self):
        try:
            with transaction.atomic():
                Book.objects.create(title="Rollback Book")
                raise Exception("Force rollback")
        except Exception:
            pass

        logs = Log.objects.all()
        print("Logs after rollback:", list(logs))