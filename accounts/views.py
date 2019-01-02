from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from foodevent.models import FoodEvent, Place, TakeFood
from accounts.models import User_extend
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request,user)
            # return redirect('articles:list')
            return redirect('../')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request,user)
            return redirect('../')
        else:
            return redirect("../")
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('../')
@login_required(login_url='/accounts/')
def profile(request):
    if request.user.is_authenticated:
        name = request.user.username
        user = request.user
        try:
            new_user = User_extend.objects.get(user=user)
        except:
            new_user = User_extend.objects.create(user=user,rating=0)
        history = TakeFood.objects.all()
        myhis = []
        mytake = []
        rat = 10
        for his in history:
            if his.food.provider == request.user:
                myhis.append(his)
        for his in history:
            if his.taker == request.user:
                mytake.append(his)
                rat = rat+his.rating
        if len(mytake) != 0:
            rat = rat/(len(mytake)+1)
        User_extend.objects.filter(user=user).update(rating=rat)
    return render(request,"accounts/profile.html",locals())

