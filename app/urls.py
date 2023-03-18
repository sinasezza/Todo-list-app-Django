from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home-page'),
    path('tasks/',views.TaskListView.as_view(),name='task-list'),
    path('task/<int:user_id>-<str:title>/',views.TaskDetailView.as_view(),name='task-detail'),

]


