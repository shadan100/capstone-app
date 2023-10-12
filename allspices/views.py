from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

from .models import Recipe, Comment, User, Favourite

def index(request):
    return render(request, 'allspices/index.html', {
        'recipe': Recipe.objects.all()
    })

def create(request):
    if request.method == 'GET':
        return render(request, 'allspices/create.html')
    else:
        res = Recipe(title= request.POST['title'],
        method=request.POST['method'],
        ingredients=request.POST['ingred'],
        description=request.POST['desc'],
        category=request.POST['cat'],
        img_url=request.POST['img_url'],
        chef=request.user)
        res.save()
        return render(request, "allspices/index.html")

def favourite(request):
    favor = Favourite.objects.filter(user=request.user)
    return render(request, 'allspices/favourite.html',{
        'favor': favor
    })

def comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        id = request.POST['id']
        user = request.user
        com = Comment(recipe=Recipe.objects.filter(id=id).first(),user=user, comment=comment)
        com.save()
        return HttpResponseRedirect(reverse('details', kwargs={'id':id}))
    
def add_favourite(request,id):
    favo = Favourite(user=request.user, recipe=Recipe.objects.get(id=id))
    favo.save()
    return HttpResponseRedirect(reverse('details',kwargs={'id':id}))

def del_favourite(request,id):
    delfavo = Favourite.objects.filter(user=request.user, recipe=Recipe.objects.get(id=id)).first()
    delfavo.delete()
    return render(request, 'allspices/favourite.html')

def category(request):
    cat = Recipe.objects.all()
    return render(request,"allspices/category.html",{'cat':cat})

def details(request,id):
    if request.method == 'GET':
        recipe = Recipe.objects.filter(id=id).first()
        favourite = None
        if(request.user.is_authenticated):
            favourite = Favourite.objects.filter(recipe=recipe,user=request.user).first()
        comment = recipe.comment_set.all()
        return render(request,"allspices/details.html",{'recipe':recipe,'comments':comment,'favor':favourite})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "allspices/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "allspices/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "allspices/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "allspices/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "allspices/register.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))