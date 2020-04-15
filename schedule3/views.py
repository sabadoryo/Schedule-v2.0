from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView

from schedule3.models import TimeTable


# class SchedulePageView(TemplateView):
#     template_name = 'schedule3/index.html'

class ModalContent(TemplateView):
    template_name = 'schedule3/event-abs-circuit.html'


class GroupTimeTableView(DetailView):
    model = TimeTable
    template_name = 'schedule3/index.html'
