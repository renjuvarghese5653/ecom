from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Category,Product,CartItem

# Create your views here.
def index(request):
    return render(request, 'index.html')

def collections(request):
    categories=Category.objects.filter(status=0)
    return render(request,'collections.html',{"categories":categories})

def loginn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
           auth.login(request,user)
           return redirect('/')
        else:
            messages.info(request,"invalid login")
    return render(request, 'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"user name already exits")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already taken")
            return redirect('register')
        else:
         user=User.objects.create_user(username=username,email=email,password=password)
         user.save();
        return redirect('/')
    else:
     return render(request, 'registerform.html')
    
def logout(request):
   auth.logout(request)
   return redirect('/')

def collectionsview(request,slug):
   if(Category.objects.filter(slug=slug,status=0)):
      product=Product.objects.filter(category__slug=slug)
   else:
      messages.error(request,"no")
      return redirect('collections')
   return render(request,'product.html',{"product":product}) 

def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0):
        if Product.objects.filter(slug=prod_slug, status=0):
            aswin = Product.objects.filter(slug=prod_slug, status=0)
        else:
            messages.error(request, "No such products")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    return render(request, "productview.html", {"aswin": aswin})



def add_to_cart(request, cate_slug, prod_slug):
    # Retrieve the product using slugs
    product = get_object_or_404(Product, category__slug=cate_slug, slug=prod_slug, status=0)
    

    # Get or create the user's cart in the session
    cart = request.session.get('cart', {})

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        cart_item = CartItem(product=product, quantity=quantity, user=request.user)
        cart_item.save()

        # Check if the item is already in the cart
        cart_item = cart.get(product.id)

        if cart_item:
            # Item already in the cart, update the quantity
            cart_item['quantity'] += quantity
            cart_item['total'] = cart_item['quantity'] * product.selling_price
            messages.success(request, f"{product.name} quantity updated in the cart.")
        else:
            # Item not in the cart, add a new entry
            cart_item = {
                'id': product.id,
                'name': product.name,
                'quantity': quantity,
                'price': product.selling_price,
                'total': quantity * product.selling_price,
                'image': product.product_image.url,
            }
            cart[product.id] = cart_item
            messages.success(request, f"{product.name} added to the cart.")

        # Save the updated cart in the session
        request.session['cart'] = cart

        # Redirect back to the product view or any other desired page
        return redirect('add_to_cart', cate_slug=cate_slug, prod_slug=prod_slug)

    # Handle GET requests if needed
    return render(request, 'add_to_cart.html',{'aswin':[product],'cart':cart})




from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import CartItem

def delete_from_cart(request,pk):
    # Get the CartItem instance
    cart_item = CartItem.objects.get(pk=pk)
    if cart_item:
        cart_item.delete()
    return redirect('add_to_cart')

    



def buy_now(request, product_slug):
    # Your code for buy now functionality goes  here
    pass