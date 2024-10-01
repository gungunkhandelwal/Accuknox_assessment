from django.shortcuts import render
from . models import *
from time import time
import threading
from django.db import transaction
from django.http import JsonResponse

def trigger_sync_signal(request):
    # Trigger the sync signal and measure the time taken
    start_time = time()
    Person.objects.create(name="Test Synchronous Signal")
    end_time = time()
    return render(request, 'sync_signal.html', {
        'time_taken': end_time - start_time
    })


def trigger_thread_signal(request):
    # Check if the signal runs in the same thread
    print(f"Main thread ID: {threading.get_ident()}")
    Person.objects.create(name="Check Thread Signal")
    return render(request, 'thread_signal.html')

def trigger_transaction_signal(request):
    try:
        with transaction.atomic(): 
            Person.objects.create(data="Initial Data")
    except Exception as e:
        print(f"Transaction rolled back: {e}")
    final_instance = Person.objects.first()
    return render(request, 'transaction_signal.html', {
        'final_data': final_instance.data if final_instance else "No data"
    })


# Custom Class

def rectangle_view(request):
    rect = Rectangle(10, 5)

    # Iterate over the rectangle instance
    iterated_data = [item for item in rect]

    # Example response
    return JsonResponse({'rectangle_data': iterated_data})
