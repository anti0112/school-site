from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.lesson_list),
    path('code/', views.code_python),
    path('code/execute_python_code/', views.execute_python_code),
]