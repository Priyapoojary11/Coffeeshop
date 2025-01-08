from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, ProfileForm
from .models import Coffee, Order, OrderItem, Profile
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def profile(request):
    
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST' and 'profile_picture' in request.FILES:
        
        # Handle profile picture change
        profile.profile_picture = request.FILES['profile_picture']
        profile.save()
        return redirect('profile')  # Reload the page to show new profile picture

    if request.method == 'POST' and 'delete_picture' in request.POST:
        
        # Handle profile picture deletion
        profile.profile_picture = None
        profile.save()
        return redirect('profile')  # Reload the page to remove profile picture
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'profile': profile, 'form': form})

# Sign up view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            
            # Create the user
            user = form.save(commit=False) 
            user.set_password(form.cleaned_data['password1'])
            user.save()  # Save the user to the database
            
            print("User created successfully:", user)  # Debugging line

            # Create the Profile for the new user
            profile = Profile.objects.create(
                user=user,  # This must pass the user object
                mobile_number=form.cleaned_data['mobile_number'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address']
            )
            print("Profile created successfully:", profile)  # Debugging line

            # Redirect to login page after successful signup
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')  # Redirect to login page after signup
        else:
            # Print form errors for debugging
            print("Form errors:", form.errors)
            return render(request, 'signup.html', {
                'form': form,
                'error_message': "Form submission error. Please correct the fields below.",
                'form_errors': form.errors  # Pass errors to template to display
            })
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    
    alert_message = None  # Message to display in the alert
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username exists
        if not User.objects.filter(username=username).exists():
            alert_message = "Enter a valid username."  # New user
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home if login is successful
            else:
                alert_message = "Invalid credentials. Please try again."
    return render(request, 'login.html', {'alert_message': alert_message})

# Home page view
@login_required
def home(request):
    username = request.user.username #if request.user.is_authenticated else "Unknown User"   # Display username if authenticated; otherwise show "Unknown User"
    coffees = Coffee.objects.all()  # Display coffee items
    response = render(request, 'home.html', {'username': username, 'coffees': coffees})
    return response

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def gallery(request):
    coffees = Coffee.objects.all()
    return render(request, 'gallery.html', {'coffees': coffees})

@login_required
def view_coffee(request, coffee_id):
    
    # Fetch the coffee with the given ID
    coffee = get_object_or_404(Coffee, id=coffee_id)
    return render(request, 'view_coffee.html' , {'coffee': coffee})

@login_required
def add_to_cart(request, product_id):
    coffee = Coffee.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('view_cart')

@login_required
def add_to_checkout(request, product_id):
    coffee = Coffee.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('checkout1')

@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        if cart[str(product_id)]>1:
            cart[str(product_id)]-=1
        else:
            del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    coffees = Coffee.objects.filter(id__in=cart.keys())
    cart_items = []
    total_cost = 0
    for coffee in coffees:
        quantity = cart[str(coffee.id)]
        cost = coffee.price * quantity
        total_cost += cost
        cart_items.append({
            'coffee': coffee,
            'quantity': quantity,
            'total_cost': cost
        })
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cost': total_cost})
    
    
@login_required
def checkout(request):
    
    # Get cart details and calculate total cost
    cart = request.session.get('cart', {})
    coffees = Coffee.objects.filter(id__in=cart.keys())
    total_cost = 0
    cart_items = []

    for coffee in coffees:
        quantity = cart[str(coffee.id)]
        cost = coffee.price * quantity
        total_cost += cost
        cart_items.append({'coffee': coffee, 'quantity': quantity, 'cost': cost})

    if request.method == "POST":
        
        # Create an order
        order = Order.objects.create(user=request.user, total_cost=total_cost)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                coffee=item['coffee'],
                quantity=item['quantity'],
                item_cost=item['cost'],
            )
        # Clear the cart
        request.session['cart'] = {}
        # print(f"Order ID after save: {order.id}") 
        messages.success(request, "Order placed successfully!")
        return redirect('payment', order_id=order.id)

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_cost': total_cost})


@login_required
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == "POST":
        # Simulate payment processing
        order.status = "Paid"  
        order.save()
        messages.success(request, "Payment successful!")
        return redirect('home')

    return render(request, 'payment.html', {'order': order})

@login_required
def checkout1(request):
    cart = request.session.get('cart', {})
    coffees = Coffee.objects.filter(id__in=cart.keys())
    total_cost = 0
    cart_items = []

    for coffee in coffees:
        quantity = cart[str(coffee.id)]
        cost = coffee.price * quantity
        total_cost += cost
        cart_items.append({'coffee': coffee, 'quantity': quantity, 'cost': cost})

    if request.method == "POST":
        
        # Create an order
        order = Order.objects.create(user=request.user, total_cost=total_cost)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                coffee=item['coffee'],
                quantity=item['quantity'],
                item_cost=item['cost'],
            )
        # Clear the cart
        request.session['cart'] = {}
        # print(f"Order ID after save: {order.id}") 
        messages.success(request, "Order placed successfully!")
        return redirect('payment', order_id=order.id)

    return render(request, 'checkout1.html', {'cart_items': cart_items, 'total_cost': total_cost})

