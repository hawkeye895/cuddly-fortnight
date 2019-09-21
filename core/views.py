import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .forms import LogMessageForm
from .models import LogMessage
from django.views.generic import ListView
# Create your views here.

# def home(request):
#     return render(request,
#     'core/home.html')

class HomeListView(ListView):
    model= LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def visitor(request):
    return render(request,
    'core/index.html')

def about(request):
    return render(request,
    'core/about.html',
    )

def contact(request):
    return render(request,
    'core/contact.html',
    )

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("core:home")
    else:
        return render(request, "core/log_message.html", {"form": form})


