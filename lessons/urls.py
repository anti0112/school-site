from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.lesson_list),
    path('code/', views.execute_python_code),
]