# pages/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Attractions, Days, ToDoItem
from .forms import AttForm, DayForm, ItemForm
from django.contrib import messages
from django.urls import reverse



class HomePageView(TemplateView):
    template_name = "home.html"

class CreateAtt(CreateView):
    model = Attractions
    form_class = AttForm
    template_name = "create_att.html"

def list_att(request):
  all_attractions = Attractions.objects.all()
  context = {"attractions" : all_attractions}
  return render(request, 'attractions.html', context)

class UpdateAtt(UpdateView):
  model = Attractions
  form_class = AttForm
  template_name = "update_att.html"


def delete_post(request, id):
    att = get_object_or_404(Attractions, pk=id)
    context = {'attraction': att}    
    
    if request.method == 'GET':
        return render(request, 'delete_att.html',context)
    elif request.method == 'POST':
        att.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('/attractions')


def details(request, id):
  attraction = get_object_or_404(Attractions, pk=id)
  context = {"attractions" : attraction, "pk" : id, "image": attraction.image, "image_of_us": attraction.image_of_us, "description": attraction.description
  , "experience":attraction.experience}
  return render(request, 'details.html', context)

def list_days(request):
  all_days = Days.objects.all()
  context = {"days" : all_days}
  return render(request, 'days.html', context)

class CreateDay(CreateView):
    model = Days
    form_class = DayForm
    template_name = "create_day.html"

def list_todo(request):
  all_days = ToDoItem.objects.all()
  context = {"to_do" : all_days}
  return render(request, 'todo_list.html', context)    

def delete_task(request, id):
    att = get_object_or_404(ToDoItem, pk=id)
    context = {'item': att}    
    
    if request.method == 'GET':
        return render(request, 'delete_item.html',context)
    elif request.method == 'POST':
        att.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('/todo')

class CreateItem(CreateView):
    model = ToDoItem
    form_class = ItemForm
    template_name = "create_item.html"

class UpdateItem(UpdateView):
    model = ToDoItem
    form_class = ItemForm
    template_name = "update_item.html"
