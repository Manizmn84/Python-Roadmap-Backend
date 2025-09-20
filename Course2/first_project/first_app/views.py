from django.shortcuts import render , HttpResponse

# Create your views here.
def signup_view(request) -> HttpResponse :
    return HttpResponse("Signup Completed!")

def say_hello(request) -> HttpResponse :
    return HttpResponse("welcome to the django app!")

def person_info(request , first_name , last_name , age) -> HttpResponse :
    return HttpResponse(f"<h1>{first_name:}\n{last_name:}\n{age:}</h1>")