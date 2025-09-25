from django.urls import path
from .views import *


urlpatterns = [
    path("say_hello/" , say_hello),
    path("signup/" , signup_view),
    path("info/<str:first_name>/<str:last_name>/<int:age>/",person_info),
    path("tasks/", list_create_tasks),
    path("author_detail/" , author_detail),
    path("new_author/" , new_author),
    path("author_list/" , AuthorListView.as_view() , name="author-list"),
    path("author_detail2/<int:pk>/" , AuthorDetailView.as_view()),
    path("create_author/" , AuthorCreatView.as_view()),
    path("update_author/<int:pk>/" , AuthorUpdateView.as_view()),
    path("delete_author/<int:pk>/" , AuthorDeleteView.as_view())
]