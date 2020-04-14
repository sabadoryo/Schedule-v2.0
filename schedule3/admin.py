from django.contrib import admin

# Register your models here.
from schedule3.models import *

admin.site.register(Event)
admin.site.register(Groups)
admin.site.register(Teacher)
admin.site.register(Subjects)
admin.site.register(TimeTable)
