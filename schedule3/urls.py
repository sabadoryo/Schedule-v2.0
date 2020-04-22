from django.urls import path

from schedule3.views import *
from . import views

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('student', StudentMainPage.as_view(), name='student_main_page'),
    path('<slug:slug>', GroupTimeTableView.as_view(), name='group_timetable'),
    path('teacher/<int:pk>', TeacherTimeTableView.as_view(), name='teacher_timetable'),
    path('<str:str>', ModalContent.as_view(), name='modal-content'),
    path('ajax/validate_username', views.validate_username, name='validate_username'),
    path('ajax/search_autocomplete', views.search_autocomplete, name='search-autocomplete'),
    path('teacher/profile', views.TeacherMainPage.as_view(), name='teacher_main_page'),
    path('teacher/profile/update/<int:pk>', EventUpdate.as_view(), name='event_update_page'),
]
