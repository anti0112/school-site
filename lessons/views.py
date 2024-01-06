from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Lesson
import subprocess

@api_view(['GET', 'POST'])
def lesson_list(request):
    if request.method == 'GET':
        lessons = Lesson.objects.all()
        serialized_lessons = [{'id': lesson.id, 'title': lesson.title} for lesson in lessons]
        return Response(serialized_lessons)
    
    elif request.method == 'POST':
        # Создание нового урока
        data = request.data
        lesson = Lesson.objects.create(title=data.get('title'), content=data.get('content'))
        return Response({'id': lesson.id, 'title': lesson.title})

@api_view(['GET'])
def code_python(request):
    if request.method == 'GET':
        return render(request, 'code-q.html')

@csrf_exempt
def execute_python_code(request):
    if request.method == 'POST':
        python_code = request.POST.get('python_code', '')

        # Выполнение кода Python
        try:
            process = subprocess.Popen(['python', '-c', python_code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate()
            if error:
                return JsonResponse({'output': '', 'error': error})
            else:
                return JsonResponse({'output': output, 'error': ''})
        except Exception as e:
            return JsonResponse({'output': '', 'error': str(e)})

    # Возврат ошибки если метод не POST
    return JsonResponse({'output': '', 'error': 'Метод не разрешен'})