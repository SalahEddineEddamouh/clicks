from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from .models import Article


# Create your views here.

@login_required(login_url='/dashboard/login')
def dashboard(request):
    return render(request,'dashboard/pages/dashboard.html')


def loginView(request):
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect("dashboard")
            
        
    return render(request,'dashboard/pages/login.html')



def logoutView(request):
    logout(request)
    return  redirect("dashboard")


def articles(request):
    return render(request,"dashboard/pages/articles.html")


def article(request):
    # articleSlug = Article.objects.get(slug=slug)
    article = {
        "id":0,
        "title":"from zero to hero",
        "content":"from zero to hero this is content",
        "created_at":"20022",
        "meta":"PUBLISHED",
        "categories":"business",
        "keywords":"from, zero, to, hero",
    }
    return render(request,"dashboard/pages/article.html",{"article":article})


def media(request):
    return render(request,"dashboard/pages/media.html")


def accounts(request):
    return render(request,"dashboard/pages/accounts.html")


def categories(request):
    return render(request,"dashboard/pages/categories.html")