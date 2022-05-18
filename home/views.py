from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'home/home.html'
    extra_context = {'time': datetime.now()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

# def home(request):
#     return render(request, 'home/home.html', {'time': datetime.now()})


# @login_required
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

