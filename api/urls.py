from django.urls import path
from . views import *

urlpatterns=[
    path('sync_signal/',trigger_sync_signal,name='sync_signal'),
    path('thread_signal/',trigger_thread_signal,name='thread_signal'),
    path('transactional_signal/',trigger_transaction_signal,name='transaction_singal'),
    path('rectangle_view/',rectangle_view,name='rectangle_view')
]