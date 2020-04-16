from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView

from schedule3.models import TimeTable, Event


# class SchedulePageView(TemplateView):
#     template_name = 'schedule3/index.html'

class ModalContent(TemplateView):

    template_name = 'schedule3/modal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.get(modal_page=self.kwargs['str'].strip('.html'))
        return context


class GroupTimeTableView(DetailView):
    model = TimeTable
    template_name = 'schedule3/index.html'
