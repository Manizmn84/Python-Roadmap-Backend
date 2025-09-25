from django.shortcuts import render , HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Task , Book ,Author , Musician
from .forms import AuthorForm
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

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

@csrf_exempt
def author_detail(request) -> render :
    if request.method == "GET" :
        authors = Author.objects.all()
        return render(request , "author_detail.html",{ 
            "authors" :authors
            })
    if request.method == "POST" :
        form = AuthorForm(request.POST)
        if not form.is_valid() :
            return HttpResponse("data is invalid")
        Author.objects.create(name=form.cleaned_data["name"])
        authors = Author.objects.all()
        return render(request , "author_detail.html",{ 
            "authors" :authors
            }) 
    
@csrf_exempt
def new_author(request) :
    if request.method == "GET" :
        author_form = AuthorForm()
        return render(request , "new_author.html" , {
            "author_form" :author_form
        })
    
    if request.method == "POST" :
        form = AuthorForm(request.POST)
        if not form.is_valid() :
            return HttpResponse("data is invalid")
        # Author.objects.create(name=form.cleaned_data["name"])
        form.save()
        authors = Author.objects.all()
        return render(request , "author_detail.html",{ 
            "authors" :authors
            }) 
    
class Musician_list(View):
    def get(self , request) :
        musicians = Musician.objects.values_list("name" , flat=True).order_by("name")
        return HttpResponse(musicians)

class AuthorListView(ListView) :
    model = Author
    template_name = "author_list.html"
    # queryset = Author.objects.filter(name__startswith="m")

class AuthorDetailView(DetailView) :
    model = Author
    template_name = "author_detail2.html"

class AuthorCreatView(CreateView) :
    model = Author
    template_name = "create_author.html"
    fields = ["name"]

class AuthorUpdateView(UpdateView) :
    model = Author
    fields = ["name"]
    template_name = "author_update.html"
    success_url = reverse_lazy("author-list")

class AuthorDeleteView(DeleteView) :
    model = Author
    template_name = "delete_author.html"
    success_url = reverse_lazy("author-list")