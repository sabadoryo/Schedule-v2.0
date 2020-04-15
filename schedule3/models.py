from django.db import models
import weekday_field
from django.utils.text import slugify

# Create your models here.
SUBJECT_TYPE = (
    ("0", 'Lecture'),
    ("1", 'Practice'),
    ("2", 'Laboratory'),
)


class Subjects(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Groups(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return 'Teacher:' + self.name + self.surname


DAYS_OF_WEEK = (
    ("0", 'Monday'),
    ("1", 'Tuesday'),
    ("2", 'Wednesday'),
    ("3", 'Thursday'),
    ("4", 'Friday'),
    ("5", 'Saturday'),
    ("6", 'Sunday'),
)


class TimeTable(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.group.title)
        super(TimeTable, self).save(*args, **kwargs)

    def __str__(self):
        return 'Timetable for:' + self.group.title


class Event(models.Model):
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    subject = models.OneToOneField(Subjects, on_delete=models.CASCADE, null=True)
    # period =
    room = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    room_number = models.IntegerField(default=0)
    type = models.CharField(max_length=20, choices=SUBJECT_TYPE, null=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True)
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE, null=True)
    modal_page = models.CharField(max_length=200, default='')

    def __str__(self):
        return 'Event for:' + self.time_table.group.title + 'for:' + str(self.start.hour) \
               + ':0' + str(self.start.minute) \
               + '- ' + \
               str(self.end.hour) + ':' + str(self.end.minute) + ', ' + self.subject.title
