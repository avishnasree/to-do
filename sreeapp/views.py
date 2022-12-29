from django.shortcuts import render, redirect

# Create your views here.
from sreeapp.forms import Todoform
from sreeapp.models import Todo


def mainpage(request):
    return render(request,'index1.html')


def addTodo(request):
    form=Todoform()
    if request.method=='POST':
        form=Todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewtodo')
    return render(request,'Todo.html',{'form':form})


def viewtodo(request):
    todos=Todo.objects.all()
    return render(request,'view.html',{'todos':todos})

def update(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    form=Todoform(instance=todo)
    if request.method=='POST':
        form=Todoform(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('viewtodo')
    return render(request,'update.html',{'form':form})

def delete(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return  redirect('viewtodo')
