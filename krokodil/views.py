from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page(request):
    days = {
        'monday': ['Задача 1', 'Задача 2'],
        'tuesday': ['Задача 3', 'Задача 4'],
        'wednesday': ['Задача 5'],
        'thursday': [],
        'friday': ['Задача 6'],
        'saturday': ['Задача 7', 'Задача 8'],
        'sunday': ['Задача 9'],
    }
    return render(request, 'index.html', {'days': days})

def day_tasks(request, day_name):
    days = {
        'monday': ['Задача 1', 'Задача 2'],
        'tuesday': ['Задача 3', 'Задача 4'],
        # ... остальные дни
    }
    tasks = days.get(day_name, [])
    return render(request, 'day.html', {'tasks': tasks, 'day': day_name})