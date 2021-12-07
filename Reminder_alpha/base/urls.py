from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasklist, name='tasks'),
    path('', views.index, name='index'),
    path('new_note', views.new_note, name='new_note'),
]