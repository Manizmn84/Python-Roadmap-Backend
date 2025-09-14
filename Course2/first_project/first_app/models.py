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