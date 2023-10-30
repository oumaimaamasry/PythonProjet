from django.shortcuts import render,redirect
from .models import sous_categorie
from categorie.models import categorie
from materiel.models import materiel
from .forms import sous_categorieform

def sous_cat(request):
    Categorie = categorie.objects.all()
    Sous_cat = sous_categorie.objects.all()
    Materiel = materiel.objects.all()
    materiel.objects.filter(pk=request.GET.get('Sous_catetorie.id'))
    cat_found = "rien"
    for c in Categorie:
        if c.id == int(request.GET.get('id')):
            cat_found = c
            break
    liste_souscat = []
    for s in Sous_cat:
        if s.Categorie == cat_found:
            liste_souscat.append(s)
    context = {'liste_souscat': liste_souscat, 'cat_found': cat_found, 'categorie': Categorie,'Materiel':Materiel,'Sous_cat':Sous_cat}
    return render(request, 'sous_categorie/sous_categorie.html',context)



def ajouter_souscategorie(request):
   form=sous_categorieform()
   if request.method=='POST':
       form=sous_categorieform(request.POST)
       if form.is_valid():
         form.save()
         return redirect('../../categorie/categorie')
   context={'form':form}
   return render(request,'sous_categorie/ajouter_souscat.html',context)


def ajouter_sous(request):
   form=sous_categorieform()
   if request.method=='POST':
       form=sous_categorieform(request.POST)
       if form.is_valid():
         form.save()
         return redirect('../../categorie/categorie')
   context={'form':form}
   return render(request,'sous_categorie/ajouter_souscat.html',context)


def modifier_souscategorie(request,pk):
    Sous_categorie=sous_categorie.objects.get(id=pk)
    form = sous_categorieform(instance=Sous_categorie)
    if request.method == 'POST':
        form = sous_categorieform(request.POST,instance=Sous_categorie)
        if form.is_valid():
            form.save()
            return redirect('../../categorie/categorie')
    context = {'form': form}
    return render(request,'sous_categorie/ajouter_souscat.html',context)


def supprimer_souscategorie(request,pk):
    Sous_categorie=sous_categorie.objects.get(id=pk)
    if request.method=='POST':
        Sous_categorie.delete()
        return redirect('../../categorie/categorie')
    context={'item':Sous_categorie}
    return render(request,'sous_categorie/supprimer_souscat.html',context)

def afficher_souscat(request):
    Souscat = sous_categorie.objects.all()
    context = {'Souscat':Souscat}
    return render(request, 'sous_categorie/afficher_souscat.html', context)
