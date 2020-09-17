from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required


@login_required
def todo_list(request):
    todo = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo1 = Todo()
            todo1.title = form.cleaned_data['title']
            form.save()
            return redirect('home:todo_list')
        else:
            form = TodoForm()

    if request.method == 'POST':
        todo_id = request.POST['todo_id']
        todo1 = get_object_or_404(Todo, id=todo_id)

        if todo1.checked:
            todo1.checked = False
            todo1.save()
        else:
            todo1.checked = True
            todo1.save()

    return render(request, 'todo.html', {'todo': todo, 'form': form})


@login_required
def update_todo(request, id):
    todo_id = Todo.objects.get(id=id)
    update_form = TodoForm(instance=todo_id)
    if request.method == 'POST':
        update_form = TodoForm(request.POST, instance=todo_id)
        if update_form.is_valid():
            todo1 = Todo()
            todo1.title = update_form.cleaned_data['title']
            update_form.save()
            return redirect('home:todo_list')
        else:
            update_form = TodoForm(instance=todo_id)
    return render(request, 'update_todo.html', {'update_form': update_form})


@login_required
def delete_todo(request, id):
    todo_id = Todo.objects.get(id=id)
    todo_id.delete()
    return redirect('home:todo_list')
