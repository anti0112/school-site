from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.lesson_list),
    path('lessons/<int:lesson_id>/run_code/', views.run_python_code),
]