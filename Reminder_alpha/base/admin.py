from django.contrib import admin
from django.contrib import admin
from .models import Notes
from .models import Task
# Register your models here.
admin.site.register(Task)
admin.site.register(Notes)
