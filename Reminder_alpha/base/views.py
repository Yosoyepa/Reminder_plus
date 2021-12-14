from django.db import models
from django.shortcuts import render, redirect
from .models import Notes, Task
from .forms import NotesForm
from django.contrib import messages
from django.views.generic.list import ListView
# Create your views here.



def index(request):
    notes = Notes.objects.all()
    return render(request, "index.html", {"notes": notes})

def new_note(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update.html", {"form": form})

def note_detail(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update.html", {"note": note, "form": form})


def delete_note(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        note.delete()
        messages.info(request, "La nota ha sido eliminada")
    return render(request, "delete.html", {"note": note, "form": form})

def search_page(request):
    if request.method == 'POST':
        search_text = request.POST['search']
        notes = Notes.objects.filter(heading__icontains = search_text) | Notes.objects.filter(text__icontains = search_text)
        # if notes is None:
        #     messages.info(request, "la nota no se ha encontrado")
        return render(request, "search.html", {"notes": notes})

## Clases:

class TaskList(ListView):
    model = Task