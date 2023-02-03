from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    path("home", views.HomePageView.as_view(), name="home"),
    path("",  views.HomePageView.as_view(), name=""),
    path("todo", views.list_todo, name="todo"),
    path("create_item", views.CreateItem.as_view(), name="create_item"),
    path("todo/<pk>/date", views.UpdateItem.as_view(), name="update_item"),
    path('todo/<id>/delete', views.delete_task, name='delete_task'),
    path("days", views.list_days, name="days"),
    path("create_day", views.CreateDay.as_view(), name="create_day"),
    path("create_att", views.CreateAtt.as_view(), name="create_att"),
    path('attractions/<id>/', views.details, name='details'),
    path("attractions", views.list_att, name="attractions"),
    path('att/<pk>/update', views.UpdateAtt.as_view(), name="update_att"),
    path('att/<id>/delete', views.delete_post, name='delete_att'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
