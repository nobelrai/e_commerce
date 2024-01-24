from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name="index.html")

def checkout(request):
    return render(request, template_name="checkout.html")

def contact(request):
    return render(request, template_name="contact.html")

def detail(request):
    return render(request, template_name="detail.html")

def shop(request):
    return render(request, template_name="shop.html")

def cart(request):
    return render(request, template_name="cart.html")