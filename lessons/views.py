from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lesson

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

@api_view(['GET', 'POST'])
def run_python_code(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    
    if request.method == 'POST':
        # Выполнение Python-кода
        code_to_execute = request.data.get('code')
        # Здесь нужно использовать библиотеку для безопасного выполнения кода, например, `exec()` или `ast.literal_eval()`
        # Важно обеспечить безопасность выполнения кода!
        try:
            result = exec(code_to_execute)
            return Response({'result': result})
        except Exception as e:
            return Response({'error': str(e)})