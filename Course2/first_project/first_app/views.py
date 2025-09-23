from django.shortcuts import render , HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task , Book

# Create your views here.
def signup_view(request) -> HttpResponse :
    return HttpResponse("Signup Completed!")

@csrf_exempt
def say_hello(request) -> HttpResponse :
    # print(request.GET)
    # print("name: " ,request.GET["name"])
    # print(request.GET.get("last_name","zamani"))
    # print(f"name : {request.POST.get("first_name")}")
    return HttpResponse(f"hello {request.POST.get("first_name")} to the django")
    # return HttpResponse("welcome to the django app!")

def person_info(request , first_name , last_name , age) -> HttpResponse :
    return HttpResponse(f"<h1>{first_name:}\n{last_name:}\n{age:}</h1>")

@csrf_exempt
def list_create_tasks(request) -> HttpResponse :
    task = request.POST.get("task")
    Task.objects.create(name=task)
    return HttpResponse(f"Task Created: '{task}'")

def delete_Task(request , task_id) -> HttpResponse :
    if request.method == "DELETE" :
        tasks = Task.objects.filter(id=task_id)
        if len(tasks) != 0 :
            task = tasks[0]
            task.delete()
            return HttpResponse(f"Task Done: '{task.name}'")
        else:
            return HttpResponse(f"There isn't any task with id '{task_id}'")  

def booklist(request) -> render :
    books = Book.objects.all()    
    return render(request , "booklist.html" , {"books" : books})      