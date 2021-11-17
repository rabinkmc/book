from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from django.views import View

from book.models import Publisher

class PublisherListView(ListView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')


