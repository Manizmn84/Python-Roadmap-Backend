from django.shortcuts import render , HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

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
