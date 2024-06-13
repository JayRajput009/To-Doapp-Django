from django.shortcuts import render
from todoapp.models import Todo


# Create your views here.

#for creating a todo
def create(request):
    if request == "POST":
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        starttime = data.get('starttime')
        endtime = data.get('endtime')

        Todo.objects.create(
            todotitle = title,
            tododesctiption = description,
            todostarttime = starttime,
            todoendtime = endtime
        )

        todorow = Todo.objects.all()
        
        



    return render(request, 'index.html')
