from django.contrib import admin
from . import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','user','title','complete','created',)



admin.site.register(models.Task,TaskAdmin)