from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import creeruser
from django.contrib import messages
# Create your views here.



def inscription(request):
    form=creeruser()
    if request.method=='POST':
        form=creeruser(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Compte crée avec succes')
            return redirect('/acces')
    context={'form':form}
    return render(request,'compte/inscription.html',context)

def acces(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('categorie/categorie')
        else:
            messages.info(request,"Nom d'utilisateur ou mot de passe incorrect")
    return render(request,'compte/acces.html',context)