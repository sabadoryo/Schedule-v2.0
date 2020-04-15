from django.urls import path

from schedule3.views import *
from . import views

urlpatterns = [
    # path('', SchedulePageView.as_view(), name='index'),
    path('<slug:slug>', GroupTimeTableView.as_view(), name='group_timetable'),
    path('event-abs-circuit.html', ModalContent.as_view(), name='modal-content')
]

