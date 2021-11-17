from django.urls import path
from book.models import Publisher

from book.views import PublisherListView, MyView
urlpatterns = [  
        path('hello',  MyView.as_view(), name='my-view'), 
        path('', PublisherListView.as_view(), name='publisher-list'), 
]

