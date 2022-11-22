from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from accounts.models import Account
from products.models import House_Product, Car_Product, Bike_Product, Furn_Product,Other_Product






@login_required(login_url='login')
def dashboard(request):
    # orders = Order.objects.order_by(
    #     '-created_at').filter(user_id=request.user.id, is_ordered=True)
    # order_count = orders.count()
    userprofile=Account.objects.get(id=request.user.id)
    context = {
        # 'orders_count': order_count,
        'userprofile':userprofile,
    }
    return render(request, 'dashboard/dash-my-profile.html', context)

@login_required(login_url='login')
def editprofile(request):
    # orders = Order.objects.order_by(
    #     '-created_at').filter(user_id=request.user.id, is_ordered=True)
    # order_count = orders.count()
    userprofile=Account.objects.get(id=request.user.id)



    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone_number = request.POST.get("tel")

        userprofile.fname=fname
        userprofile.lname=lname
        userprofile.phone_number=phone_number
        userprofile.save()
        return redirect('myprofile')

    context = {
        # 'orders_count': order_count,
        'userprofile':userprofile,
    }
    return render(request, 'dashboard/dash-edit-profile.html', context)


@login_required(login_url='login')
def changePassword(request):
    if request.method == 'POST':
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']

        user=Account.objects.get(email__exact=request.user.email)

        if new_password == confirm_password:
            success=user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                # auth.logout(request)
                messages.success(request, 'Password change Successfully')
                return redirect('changePassword')
            else:
                messages.success(request, 'Please enter valid current password')
                return redirect('changePassword')
        else:
            messages.error(request, 'Password does not match')
            return redirect('changePassword')
    return render(request, 'dashboard/change_password.html')



@login_required(login_url='login')
def myproducts(request, category_slug=None):

    # if request.user.is_authenticated:
    c_products = Car_Product.objects.all().filter(user=request.user.id)
    h_products = House_Product.objects.all().filter(user=request.user.id)
    b_products = Bike_Product.objects.all().filter(user=request.user.id)
    f_products = Furn_Product.objects.all().filter(user=request.user.id)
    o_products = Other_Product.objects.all().filter(user=request.user.id)



    context = {
        'h_products' : h_products,
        'c_products': c_products,
        'b_products' : b_products,
        'f_products' : f_products,
        'o_products' : o_products,


    }
    return render(request, 'dashboard/myproducts.html', context)

def managehouse(request,house_id):
    h_product = House_Product.objects.get(id=house_id)
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

        h_product.type=type
        h_product.furnish=furnish
        h_product.bedroom=bedroom
        h_product.bathroom=bathroom
        h_product.builtup=builtup
        h_product.capacity=capacity
        h_product.rent=rent
        h_product.ad_title=ad_title
        h_product.add_info=add_info
        h_product.images=images
        h_product.state=state
        h_product.city=city
        h_product.location=location
        h_product.save()
        messages.success(request, 'your product details is updated...!')
        return redirect('myproducts')




    context = {
        'h_product': h_product,

    }
    return render(request, 'dashboard/dash-edit-house-products.html', context)

def managecar(request,car_id):
    c_product = Car_Product.objects.get(id=car_id)
    # if request.method=="POST":
    #     type=request.POST('type')
    #     furnish=request.POST('furnish')
    #     bedroom=request.POST('bedroom')
    #     bathroom=request.POST('bathroom')
    #
    #     builtup = request.POST('builtup')
    #     capacity = request.POST('capacity')
    #     rent = request.POST('rent')
    #     ad_title = request.POST('ad_title')
    #     add_info = request.POST('add_info')
    #     images=request.FILES['images']
    #     state = request.POST('state')
    #     city = request.POST('city')
    #     location = request.POST('location')
    #
    #     h_product.type=type
    #     h_product.furnish=furnish
    #     h_product.bedroom=bedroom
    #     h_product.bathroom=bathroom
    #     h_product.builtup=builtup
    #     h_product.capacity=capacity
    #     h_product.rent=rent
    #     h_product.ad_title=ad_title
    #     h_product.add_info=add_info
    #     h_product.images=images
    #     h_product.state=state
    #     h_product.city=city
    #     h_product.location=location
    #     h_product.save()
    #     messages.success(request, 'your product details is updated...!')



    context = {
        'c_product': c_product,

    }
    return render(request, 'dashboard/dash-edit-car-products.html', context)

def managebike(request,bike_id):
    b_product = Bike_Product.objects.get(id=bike_id)
    # if request.method=="POST":
    #     type=request.POST('type')
    #     furnish=request.POST('furnish')
    #     bedroom=request.POST('bedroom')
    #     bathroom=request.POST('bathroom')
    #
    #     builtup = request.POST('builtup')
    #     capacity = request.POST('capacity')
    #     rent = request.POST('rent')
    #     ad_title = request.POST('ad_title')
    #     add_info = request.POST('add_info')
    #     images=request.FILES['images']
    #     state = request.POST('state')
    #     city = request.POST('city')
    #     location = request.POST('location')
    #
    #     h_product.type=type
    #     h_product.furnish=furnish
    #     h_product.bedroom=bedroom
    #     h_product.bathroom=bathroom
    #     h_product.builtup=builtup
    #     h_product.capacity=capacity
    #     h_product.rent=rent
    #     h_product.ad_title=ad_title
    #     h_product.add_info=add_info
    #     h_product.images=images
    #     h_product.state=state
    #     h_product.city=city
    #     h_product.location=location
    #     h_product.save()
    #     messages.success(request, 'your product details is updated...!')



    context = {
        'b_product': b_product,

    }
    return render(request, 'dashboard/dash-edit-bike-products.html', context)

def managefurniture(request,furniture_id):
    f_product = Furn_Product.objects.get(id=furniture_id)
    # if request.method=="POST":
    #     type=request.POST('type')
    #     furnish=request.POST('furnish')
    #     bedroom=request.POST('bedroom')
    #     bathroom=request.POST('bathroom')
    #
    #     builtup = request.POST('builtup')
    #     capacity = request.POST('capacity')
    #     rent = request.POST('rent')
    #     ad_title = request.POST('ad_title')
    #     add_info = request.POST('add_info')
    #     images=request.FILES['images']
    #     state = request.POST('state')
    #     city = request.POST('city')
    #     location = request.POST('location')
    #
    #     h_product.type=type
    #     h_product.furnish=furnish
    #     h_product.bedroom=bedroom
    #     h_product.bathroom=bathroom
    #     h_product.builtup=builtup
    #     h_product.capacity=capacity
    #     h_product.rent=rent
    #     h_product.ad_title=ad_title
    #     h_product.add_info=add_info
    #     h_product.images=images
    #     h_product.state=state
    #     h_product.city=city
    #     h_product.location=location
    #     h_product.save()
    #     messages.success(request, 'your product details is updated...!')



    context = {
        'f_product': f_product,

    }
    return render(request, 'dashboard/dash-edit-furniture-products.html', context)

def manageother(request,other_id):
    o_product = Other_Product.objects.get(id=other_id)
    if request.method=="POST":
        type = request.POST.get('type')

        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        # images = request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
    #
        o_product.type=type
        o_product.rent=rent
        o_product.ad_title=ad_title
        o_product.add_info=add_info
        # o_product.images=images
        o_product.state=state
        o_product.city=city
        o_product.location=location
        o_product.save()
        messages.success(request, 'your product details is updated...!')
        return redirect('myproducts')



    context = {
        'o_product': o_product,

    }
    return render(request, 'dashboard/dash-edit-other-products.html', context)

