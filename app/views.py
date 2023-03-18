from django.shortcuts import render , HttpResponse
from django.views.generic import View , ListView , DetailView , CreateView , UpdateView , DetailView
from . import models

class HomePageView(View):
    def get(self,request,*args, **kwargs):
        return render(request,template_name='Home/home.html')
# ===================================
class TaskListView(ListView):
    model = models.Task
    template_name = 'app_pages/task_list.html'
    context_object_name = 'tasks'
# ===================================
class TaskDetailView(DetailView):
    model = models.Task
    template_name = 'app_pages/task_detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'user_id'



