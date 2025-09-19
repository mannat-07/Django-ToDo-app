from django.shortcuts import render, redirect
from django.urls import reverse  # Add this import for URL building
from .models import Task

def home_view(request):
    """Main view for displaying, adding, toggling, and deleting tasks"""
    if request.method == "POST":
        # Check the action type
        action = request.POST.get('action')
        task_id = request.POST.get('task_id')
        
        if action == 'toggle' and task_id:
            # Toggle task completion
            try:
                task = Task.objects.get(id=task_id)
                task.completed = not task.completed
                task.save()
            except Task.DoesNotExist:
                pass  # Task not found, do nothing
            # Use reverse() to build URL with query params
            url = reverse('home') + '?success=toggle'
            return redirect(url)
        
        elif action == 'delete' and task_id:
            # Delete task
            try:
                task = Task.objects.get(id=task_id)
                task.delete()
                # Fixed: Use reverse() for proper URL construction
                url = reverse('home') + '?deleted=1'
                return redirect(url)
            except Task.DoesNotExist:
                pass  # Task not found, continue to redirect
        
        else:
            # Add new task
            new_task = request.POST.get('task')
            if new_task:
                Task.objects.create(name=new_task)
                # Fixed: Use reverse() for proper URL construction
                url = reverse('home') + '?success=1'
                return redirect(url)
        
        # If no valid action, still redirect
        return redirect('home')
    
    # GET request - show the page
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'tasks': tasks})