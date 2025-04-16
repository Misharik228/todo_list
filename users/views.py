from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todo.models import Task

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'total_tasks': tasks.count(),
        'completed_tasks': tasks.filter(completed=True).count(),
        'pending_tasks': tasks.filter(completed=False).count()
    }
    return render(request, 'users/profile.html', context)
