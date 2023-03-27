from django.shortcuts import render , HttpResponse ,redirect
from django.views.generic import View , ListView , DetailView , CreateView , UpdateView , DetailView , DeleteView , FormView
import django.contrib.auth.views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from . import models

class HomePageView(View):
    def get(self,request,*args, **kwargs):
        return render(request,template_name='Home/home.html')
# ===================================
class TaskListView(LoginRequiredMixin,ListView):
    model = models.Task
    template_name = 'app_pages/task_list.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['numbers_of_incomplete_tasks'] = context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input :
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        
        context['search_input'] = search_input
        
        return context
    
# ===================================

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = models.Task
    template_name = 'app_pages/task_detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

# ===================================

class TaskCreateView(CreateView):
    model = models.Task
    template_name = 'forms/task_create_form.html'
    fields = ['title','description','complete']
    success_url = reverse_lazy('app:task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView,self).form_valid(form)

# ===================================

class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['title','description','complete']
    template_name = 'forms/task_update_form.html'
    success_url = reverse_lazy('app:task-list')
    

# ===================================

class TaskDeleteView(DeleteView):
    model = models.Task
    template_name = 'forms/task_delete_form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('app:task-list')
    
# ===================================

class SigninView(FormView):
    template_name = 'forms/signup_form.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('app:task-list')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(SigninView,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('app:task-list')
        return super(SigninView,self).get(*args, **kwargs)
        
# ===================================

class LoginView(auth_views.LoginView):
    template_name = 'forms/login_form.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('app:task-list')

# ===================================

class LogoutView(auth_views.LogoutView):
    next_page = 'app:login'
    


    




