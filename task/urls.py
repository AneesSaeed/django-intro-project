from django.urls import path

from task import views

from .views import TaskView

app_name = 'task'
urlpatterns = [
    path('', TaskView.as_view(), name='index'),
    path('<int:pk>/delete', views.delete , name='delete'),
    path('create/', views.create , name='create'),
    path('create/<int:pk>/', views.create , name='create_for_dev'),
]