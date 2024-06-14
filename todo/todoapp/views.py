from django.shortcuts import redirect, render
from todoapp.models import Todo


# Create your views here.

#for creating a todo
def create(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        starttime = data.get('starttime')
        endtime = data.get('endtime')

        Todo.objects.create(
            todotitle = title,
            tododescription = description,
            todostarttime = starttime,
            todoendtime = endtime
        )

    queryset = Todo.objects.all()

    return render(request, 'index.html', context={'todo':queryset})


#for delete and element

def delete(request,id):
    queryset = Todo.objects.get(id = id)
    queryset.delete()
    return redirect('/')


#for update and element

def update(request, id):
    queryset = Todo.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        starttime = data.get('starttime')
        endtime = data.get('endtime')

        queryset.todotitle = title
        queryset.tododescription = description
        queryset.todostarttime = starttime
        queryset.todoendtime = endtime

        queryset.save()

        return redirect('/')
    
    # queryset = Todo.objects.all()
    

    return render(request, 'update.html',context={'todo':queryset})



    


