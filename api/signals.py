from django.db.models.signals import post_save
from django.dispatch import receiver
import time
from . models import *
import threading

# Ques 1:Signal is synchronous
@receiver(post_save,sender=Person)
def slow_signal_handler(sender,instance,**kwargs):
    print("Signal handler started")
    time.sleep(5)
    print("signal handler finished")


# Signal Handler for Question 2: Same Thread Check
@receiver(post_save, sender=Person)
def check_thread(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")



# Ques 3:same database transaction
@receiver(post_save, sender=Person)
def transaction_signal_handler(sender, instance, **kwargs):
    print("Signal handler modifying data")
    instance.data = "Modified by signal"
    instance.save() 
    raise Exception("Trigger rollback")


