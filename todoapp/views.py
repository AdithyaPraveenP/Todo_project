from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView




# Create your views here.
class Tasklistview(ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "task1"

class TaskDetailview(DetailView):
    model = Task
    template_name = "detail.html"
    context_object_name = 'task'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = "task"
    fields = ('name',"priority","date")
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



def home(request):
    if request.method == "POST":
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        if name and priority != None:
            task = Task(name=name,priority=priority,date=date)
            task.save()

    task1 = Task.objects.all()

    return render(request, 'home.html',{'task1':task1})

def add(request):

    return render(request,"home.html")

# def detail(request):
#
#     return render (request,'detail.html',)

def test(request):
    return render(request,'test.html')

def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect ("/")


    return render(request,'delete.html')

def update(request,id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():

        f.save()
        return redirect('/')
    return render (request,'edit.html',{'f':f,"task":task})






