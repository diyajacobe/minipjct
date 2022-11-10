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

def managemypd(request):
    h_products = House_Product.objects.all().filter(user=request.user.id,)

    context = {
        'h_products': h_products,

    }
    return render(request, 'dashboard/dash-edit-myproducts.html', context)

