from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import InstagramPost, Product

def home(request):
    featured = Product.objects.filter(featured=True, available=True)[:6]
    products = Product.objects.filter(available=True)[:6]
    instagram_posts = InstagramPost.objects.filter(is_published=True)[:3]
    return render(request, "home.html", {"featured": featured, "products": products, "instagram_posts": instagram_posts})

def blog(request):
    posts = InstagramPost.objects.filter(is_published=True)
    page_obj = Paginator(posts, 9).get_page(request.GET.get("page"))
    return render(request, "blog.html", {"page_obj": page_obj})

def products(request):
    category = request.GET.get("category")
    qs = Product.objects.filter(available=True)
    if category:
        qs = qs.filter(category=category)
    return render(request, "products.html", {"products": qs, "active_category": category})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related = Product.objects.filter(category=product.category, available=True).exclude(pk=product.pk)[:3]
    return render(request, "product_detail.html", {"product": product, "related": related})

def about(request):
    return render(request, "about.html")

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Thank you. Your message has been received. We will get back to you soon.")
        return redirect("contact")
    return render(request, "contact.html", {"form": form})
