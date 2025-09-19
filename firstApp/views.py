from django.shortcuts import render
from django.http import HttpResponseRedirect

tasks = []  # Simple in-memory storage (replace with a model later)

def home_view(request):
    if request.method == "POST":
        new_task = request.POST.get('task')
        if new_task:
            tasks.append(new_task)
    return render(request, 'home.html', {'tasks': tasks})