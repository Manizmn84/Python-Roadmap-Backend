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
    library = models.ForeignKey(Library , on_delete=models.CASCADE,related_name="personals")

class Brand(models.Model):
    name = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=32, default='9T Pro', unique=True)
    price = models.PositiveIntegerField(default=2097152)
    color = models.CharField(max_length=16, default='Black')
    display_size = models.SmallIntegerField(default=4)
    is_available = models.BooleanField(default=True)
    made_in = models.CharField(max_length=20, default='China')

    def __str__(self):
        return '{} {}'.format(self.brand.name, self.model)

