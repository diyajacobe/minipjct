from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from .models import House_Product
from .models import Car_Product



def Category(request):

    return render(request, 'category.html')

@login_required(login_url='login')
def add_house(request):
    current_user = request.user
    if request.method=="POST":
        type=request.POST.get('type')
        furnish=request.POST.get('furnish')
        bedroom=request.POST.get('bedroom')
        bathroom=request.POST.get('bathroom')

        builtup = request.POST.get('builtup')
        capacity = request.POST.get('capacity')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        house=House_Product(user=current_user,type=type,furnish=furnish,bedroom=bedroom,bathroom=bathroom,builtup=builtup,capacity=capacity,
                            rent=rent,state=state,city=city,location=location,ad_title=ad_title,add_info=add_info,images=images,)
        house.save()
        messages.success(request, 'Your product is kept for rent!')

        return redirect('shop')
    return render(request, 'add_house.html')




@login_required(login_url='login')
def add_car(request):
    current_user = request.user
    if request.method=="POST":
        brand=request.POST.get('brand')
        fuel=request.POST.get('fuel')
        driven=request.POST.get('driven')
        own=request.POST.get('own')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        car=Car_Product(user=current_user,brand=brand,fuel=fuel,driven=driven,own=own,
                            rent=rent,ad_title=ad_title,add_info=add_info,images=images,state=state,city=city,location=location)
        car.save()
        messages.success(request, 'Your product is kept for rent!')

        return redirect('shop')
    return render(request, 'add_car.html')


from django.shortcuts import render, redirect

# Create your views here.
from .models import  Bike_Product

@login_required(login_url='login')
def add_bike(request):
    current_user = request.user
    if request.method=="POST":
        brand=request.POST.get('brand')
        driven=request.POST.get('driven')
        own=request.POST.get('own')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        bike=Bike_Product(user=current_user,brand=brand,driven=driven,own=own,
                            rent=rent,ad_title=ad_title,add_info=add_info,images=images,state=state,city=city,location=location)
        bike.save()
        messages.success(request, 'Your product is kept for rent!')

        return redirect('shop')
    return render(request, 'add_bike.html')

from .models import Furn_Product


@login_required(login_url='login')
def add_furn(request):
    current_user = request.user
    if request.method=="POST":
        type = request.POST.get('type')

        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        furniture=Furn_Product(user=current_user,type=type,rent=rent,ad_title=ad_title,add_info=add_info,images=images,
                               state=state,city=city,location=location)
        furniture.save()
        messages.success(request, 'Your product is kept for rent!')

        return redirect('shop')
    return render(request, 'add_furn.html')


from .models import Other_Product


@login_required(login_url='login')
def add_other(request):
    current_user = request.user
    if request.method=="POST":
        type = request.POST.get('type')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        other=Other_Product(user=current_user,type=type,rent=rent,ad_title=ad_title,add_info=add_info,images=images,
                            state=state,city=city,location=location)
        other.save()
        messages.success(request, 'Your product is kept for rent!')

        return redirect('/')
    return render(request, 'add_other.html')

