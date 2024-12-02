from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpRequest, HttpResponse
from .models import Todo
from .forms import TodoForm
# Create your views here.
@login_required
def todo_main(request: HttpRequest) -> HttpResponse:
    context = {
        'todos': Todo.objects.filter(user=request.user),
        'form': TodoForm(),
    }
    return render(request, template_name="tools/todo.html", context=context)

@login_required
@require_POST
def submit_todo(request: HttpRequest) -> HttpResponse:
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()

        context = {'todo': todo}
        return render(request, template_name="tools/todo.html#todoitem-partial", context=context)
    
@login_required
@require_POST
def complete_todo(request: HttpRequest, pk: int) -> HttpResponse:
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    context = {'todo': todo}
    return render(request, template_name="tools/todo.html#todoitem-partial", context=context)

@login_required
@require_http_methods(["DELETE"])
def delete_todo(request: HttpRequest, pk: int) -> HttpResponse:
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    response = HttpResponse(status=204)
    response["HX-Trigger"] = 'delete-todo'
    return response