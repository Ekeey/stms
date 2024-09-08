from django.urls import path
from . import views  # This imports the views.py file in the current directory


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
]
