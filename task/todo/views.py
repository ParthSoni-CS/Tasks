from django.shortcuts import render, redirect
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", max_value=11, min_value=2)


tasks = ['Django', 'Gym', 'ML']


def home(request):
    return render(request, 'todo/index.html', {
        'tasks': tasks
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks.append(form.cleaned_data["task"])
            return redirect("home")

        else:
            render(request, 'todo/add.html', {
                'form': form
            })

    return render(request, 'todo/add.html', {
        'form': NewTaskForm()
    })

# Create your views here.
