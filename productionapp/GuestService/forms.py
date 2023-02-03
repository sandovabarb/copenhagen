from django import forms
from django.forms import ModelForm
from .models import Attractions, Days, ToDoItem


class DateInput(forms.DateInput):
    input_type = 'date'


class AttForm(ModelForm):
    class Meta:
        model = Attractions
        fields = "__all__"

class DayForm(ModelForm):
    class Meta:
        model = Days
        fields = "__all__"

class ItemForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = "__all__"

