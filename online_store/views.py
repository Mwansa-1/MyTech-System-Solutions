from django.shortcuts import render , redirect ,get_object_or_404
from .forms import ProfileForm ,SearchForm
from .models import Category , Product , Cart , Profile , Order 
from django.contrib.auth.decorators import login_required
from django.db import transaction


# Create your views here.

def online_store(request):
    return render(request,'online_store/online_store.html',{
        'title': Product.objects.all()
    })

def category(request):
    return render(request,'online_store/category.html',{
        'title': Category.objects.all()
    })

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,'online_store/profile.html',{
        'title': Profile.objects.all(),
        'order': Order.objects.filter(user=request.user).order_by('-order_date'),
        # 'received': ReceivedItem.objects.filter(user=request.user),
    })

@login_required(login_url='/accounts/login/')
def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the current user
            user = request.user

            # Create or get the associated profile
            profile_instance, created = Profile.objects.get_or_create(user=user)

            # Update the profile fields with the form data
            profile_instance.address = form.cleaned_data['address']
            profile_instance.phone = form.cleaned_data['phone']

            # Check if an image was provided before updating
            if 'image' in request.FILES:
                profile_instance.image = form.cleaned_data['image']

            # Save the updated profile
            profile_instance.save()

            return redirect('profile')
    else:
        form = ProfileForm()

    return render(request, "online_store/editprofile.html", {"form": form})
####### CART VIEWS #############

@login_required(login_url='/accounts/login/')
def add_to_cart(request, id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)  # Default to 1 if quantity is not provided
        product = get_object_or_404(Product, id=id)

        # Check if the product is already in the user's cart
        existing_cart_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_cart_item:
            # If the product is already in the cart, update the quantity
            existing_cart_item.quantity += int(quantity)
            existing_cart_item.save()
        else:
            # If the product is not in the cart, create a new cart item
            cart_item = Cart(user=request.user, product=product, quantity=int(quantity))
            cart_item.save()

    return redirect('view_cart')

@login_required(login_url='/accounts/login/')
def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')
    


@login_required(login_url='/accounts/login/')
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    with transaction.atomic():  # Use atomic transaction to ensure consistency
        for cart_item in cart_items:
            product = cart_item.product
            quantity_ordered = cart_item.quantity

            if product.quantity >= quantity_ordered > 0:
                Order.objects.create(user=request.user, product=product, quantity=quantity_ordered)
                product.quantity -= quantity_ordered

                if product.quantity == 0:
                    product.availability = False

                product.save()

        cart_items.delete()

    return redirect('order')

@login_required(login_url='/accounts/login/')
def order(request):
   
    orders = Order.objects.filter(user=request.user).order_by('-order_date')

    return render(request, "online_store/orders.html" , {'orders':orders , })
    

@login_required(login_url='/accounts/login/')
def view_cart(request):
    
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    
    cart_items = Cart.objects.filter(user=request.user)

    total = 0
    subtotal = 0
    shipping = 0
    for order in orders :
        for cart_item in cart_items:
            total = float(order.product.price) * float(cart_item.quantity) + float(order.product.shipping)

    for cart_item in cart_items:
        quantity = cart_item.quantity
        price = cart_item.product.price
        shipping += float(cart_item.product.shipping)  # Ensure it's converted to float
        subtotal += quantity * price

    grand_total = subtotal + shipping

    return render(request, 'online_store/cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'grand_total': grand_total,
        'total':total
    })

####### PRODUCT VIEWS #############
def product(request):
    return render(request,'online_store/product.html',{
        'title': Product.objects.all()
    })

def product_details(request,id):
    return render(request , "online_store/product_details.html" ,{
        "title" : Product.objects.get(pk=id),
    })

####### CATEGORY VIEWS #############
def category_details(request,id):
    return render(request , "online_store/category_details.html" ,{
        "title" : Category.objects.get(pk=id),
        "list" : Product.objects.all(),
    })

####### SEARCH VIEWS #############

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)  # Example search by book title
        else:
            results = []
    else:
        form = SearchForm()
        results = []

    return render(request, 'online_store/search.html', {'form': form, 'results': results})

def signupsuccessful(request):
    return render(request , "online_store/signupsuccessful.html",{'title': Profile.objects.all(),})