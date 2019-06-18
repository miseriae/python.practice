from django.shortcuts import render, redirect
from .models import BlogPost, BlogPostCategory, BlogPostSeries
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


def single_slug(request, single_slug):
    categories = [c.category_slug for c in BlogPostCategory.objects.all()]
    if single_slug in categories:
        matching_series = BlogPostSeries.objects.filter(post_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            part_one = BlogPost.objects.filter(post_series__post_series=m.post_series).earliest("post_published")
            series_urls[m] = part_one.post_slug

        return render(request=request,
                      template_name="main/category.html",
                      context={"part_ones": series_urls})
    
    posts = [p.post_slug for p in BlogPost.objects.all()]
    if single_slug in posts:
        return HttpResponse(f"{single_slug} is a post!")

    return HttpResponse(f"{single_slug} does not correspond to anything")


def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories": BlogPostCategory.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created: {username}")
            login(request, user)
            messages.info(request, f"Logged in as: {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")


    form = NewUserForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as: {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})    