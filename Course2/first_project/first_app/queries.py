from .models import Brand, Mobile
from django.db.models import QuerySet

def list_all_brands() -> QuerySet:
    query = Brand.objects.all()
    return query

def list_all_mobiles() -> QuerySet:
    query = Mobile.objects.all()
    return query

def price_of_mobile_with_model(modelname) -> int:
    mobile = Mobile.objects.get(model=modelname)
    return mobile.price

def most_expensive_mobile() -> Mobile:
    highest_price = max(Mobile.objects.values_list("price" , flat=True))
    mobile = Mobile.objects.get(price = highest_price)
    return mobile

def all_mobiles_with_brand_of(brand_name) -> QuerySet:
    query = Mobile.objects.filter(brand__name = brand_name)
    return query

def all_available_mobiles_with_price_in_range(min_price, max_price) -> int:
    query = Mobile.objects.filter(price__lte = max_price , price__gte = min_price , is_available=True)
    return query.count() 

from django.db.models import Sum, Min, Max, Avg
def total_value_of_products():
    query = Mobile.objects.aggregate(total_value= Sum('price'))
    return query


def total_value_of_products_with_brand_of(brand_name):
    query = Mobile.objects.filter(brand__name= brand_name).aggregate(total_value= Sum('price'))
    return query


def most_expensive_cheapest_price_with_nationality_of(nationality):
    query = Mobile.objects.filter(brand__nationality= nationality).aggregate(cheap= Min('price'), expensive= Max('price'))
    return query


def display_size_avg_in_available_mobiles_between_price(minimum, maximum):
    query = Mobile.objects.filter(price__gte= minimum, price__lte= maximum, is_available= 1).aggregate(avg= Avg('display_size'))
    return query