# Create your models here.
import datetime
from django.utils import timezone
from django.db import models
from django.urls import reverse


class Days(models.Model):
    DATE_CHOICES = (("Day 1", '13. 2. 2023'),

                    ("Day 2", '14. 2. 2023'),

                    ('Day 3', '15. 2. 2023'),

                    ('Day 4', '16. 2. 2023'),

                    ('Day 5', '17. 2. 2023'),

                    ('Day 6', '18. 2. 2023')
                    )

    day_name = models.CharField(
        max_length=25, choices=DATE_CHOICES, unique=True)

    def get_absolute_url(self):
        return "/days"

    def __str__(self) -> str:
        return self.day_name


class Attractions(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000, default='', blank=True)
    image = models.ImageField(
        upload_to='GuestService/static',  default='', blank=True)
    day = models.ForeignKey(Days, on_delete=models.CASCADE)
    stop_number = models.PositiveIntegerField(default=0)
    image_of_us = models.ImageField(
        upload_to='GuestService/static', default='', blank=True)
    experience = models.CharField(max_length=2000, default='', blank=True)

    def __str__(self) -> str:
        return (self.name + '-' + self.stop_number + '-' + self.day.day_name)

    def get_absolute_url(self):
        return "/attractions"


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/todo"

    def __str__(self):
        return f"{self.title}, {self.due_date}, {self.done}"
