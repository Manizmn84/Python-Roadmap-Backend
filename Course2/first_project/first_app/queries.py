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