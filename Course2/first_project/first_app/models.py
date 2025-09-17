from django.db import models

class Person(models.Model) :
    GENDER_CHOICE = (
        ("m" , "male"),
        ("f" , "female"),
    )
    name = models.CharField(max_length=20 , blank=False)
    age = models.IntegerField(default=18)
    country = models.CharField(max_length=10 , null=True)
    gender = models.CharField(choices=GENDER_CHOICE , default="m")

class Author(models.Model) :
    name = models.CharField(max_length=100)

class Book(models.Model) :
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

class Profile(models.Model) :
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Library(models.Model) :
    number = models.PositiveIntegerField()

class Personal(models.Model) :
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    library = models.ForeignKey(Library , on_delete=models.CASCADE)