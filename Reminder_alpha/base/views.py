from django.shortcuts import render
from django.http import HttpResponse

## General Views For Users:
def index(request):
    return render(request, 'index.html', {})

def new_note(request):
    return render(request, 'new_note.html', {})

def tasklist(request):
    return HttpResponse('To do List')