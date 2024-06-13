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

def delete(requet,id):
    queryset = Todo.objects.get(id = id)
    queryset.delete()
    return redirect('/')
