from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.dashboard,name='dashboard'),
    path("login",views.loginView,name='login'),
    path("lougout",views.logoutView,name='logout'),
    path("articles",views.articles,name='articles'),
    path("article",views.article,name='article'),
    path("categories",views.categories,name='categories'),
    path("media",views.media,name='media'),
    path("accounts",views.accounts,name='accounts'),
]
