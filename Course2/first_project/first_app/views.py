from django.shortcuts import render , HttpResponse

# Create your views here.
def signup_view(request) -> HttpResponse :
    return HttpResponse("Signup Completed!")

def say_hello(request) -> HttpResponse :
    return HttpResponse("welcome to the django app!")