from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home-page'),
    path('tasks/',views.TaskListView.as_view(),name='task-list'),
    path('task/<str:user_name>-<int:task_id>-<str:title>/',views.TaskDetailView.as_view(),name='task-detail'),
    path('task-create/',views.TaskCreateView.as_view(),name='task-create'),
    path('task-update/<int:pk>',views.TaskUpdateView.as_view(),name='task-update'),
    path('task-delete/<int:pk>',views.TaskDeleteView.as_view(),name='task-delete'),
    path('signup/',views.SigninView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/<int:pk>/',views.LogoutView.as_view(),name='logout'),
    
]


