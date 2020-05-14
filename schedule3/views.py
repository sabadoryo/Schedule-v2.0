import json

import simplejson as simplejson
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, FormView, ListView, UpdateView
from itertools import chain
from schedule3.models import TimeTable, Event, Teacher, Groups
from schedule3.forms import *


def search_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        data1 = Teacher.objects.filter(name__startswith=q).values_list('name')
        data2 = Groups.objects.filter(title__startswith=q).values_list('title')
        # data3 = Event.objects.filter(room_number__exact=kek).values_list('room_number')
        data = chain(data1, data2)
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")


def selectOptionsParameters(request):
    stop = request.GET.get('speciality', None)
    course = request.GET.get('course', None)

    groups = Groups.objects.filter(title__startswith=stop, course__exact=course).values_list('title')
    showroom_list = list(groups.values('title', 'title'))

    return HttpResponse(simplejson.dumps(showroom_list), content_type="application/json")


def validate_username(request):
    search_string = request.GET.get('search_string', None)
    buk = False
    if Teacher.objects.filter(name=search_string).exists():
        teach_pk = Teacher.objects.get(name=search_string).pk
        buk = True
    elif Teacher.objects.filter(surname=search_string).exists():
        teach_pk = Teacher.objects.get(surname=search_string).pk
        buk = True
    else:
        teach_pk = None

    data = {
        'is_group': TimeTable.objects.filter(slug=search_string).exists(),
        'is_teacher': buk,
        'teacher_id': teach_pk

    }
    return JsonResponse(data)


class StudentMainPage(FormView):
    template_name = 'schedule3/student_main.html'
    form_class = SearchForm

    # success_url = 'group_time_table'
    def get_success_url(self, search_string=None):
        # find your next url here
        if TimeTable.objects.filter(slug=search_string).exists():
            return search_string
        if Teacher.objects.filter(name=search_string).exists():
            return 'group/{}'.format(search_string)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        search_string = form.cleaned_data['search_string']
        return HttpResponseRedirect(self.get_success_url(search_string))


class MainPage(TemplateView):
    template_name = 'schedule3/main.html'


# class SchedulePageView(TemplateView):
#     template_name = 'schedule3/index.html'

class ModalContent(TemplateView):
    template_name = 'schedule3/modal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.get(pk=self.kwargs['str'].strip('.html'))
        return context


class GroupTimeTableView(DetailView):
    model = TimeTable
    template_name = 'schedule3/index.html'


class TeacherTimeTableView(DetailView):
    model = Teacher
    template_name = 'schedule3/index_teacher.html'


class TeacherMainPage(ListView):
    template_name = 'schedule3/teacher_main.html'
    model = Teacher

    def get_context_data(self, **kwargs):
        context = super(TeacherMainPage, self).get_context_data(**kwargs)
        user = self.request.user
        context['eventss'] = Teacher.objects.get(email=user.username)
        print(context)
        return context


class EventUpdate(UpdateView):
    model = Event
    fields = ['message']
    template_name_suffix = '_update_form'
