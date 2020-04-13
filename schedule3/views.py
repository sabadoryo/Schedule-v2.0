from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class SchedulePageView(TemplateView):
    template_name = 'schedule3/index.html'
