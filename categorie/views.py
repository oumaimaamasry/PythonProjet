from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import categorie
from sous_categorie.models import sous_categorie
from .forms import categorieform
from materiel.filters import materielfiltre
from materiel.models import materiel
# Create your views here.
def Categorie(request):
   Materiel = materiel.objects.all()
   Categorie=categorie.objects.all()
   Sous_cat= sous_categorie.objects.all()
   sous_categorie.objects.filter(pk=request.GET.get('Categorie.id'))
   myFilter=materielfiltre(request.GET,queryset=Materiel)
   Materiel=myFilter.qs
   context={'Categorie':Categorie , 'Sous_cat': Sous_cat,'myFilter':myFilter,'Materiel':Materiel}
   return render(request, 'categorie/categorie.html', context)




def ajouter_categorie(request):
   form=categorieform()
   if request.method=='POST':
       form=categorieform(request.POST)
       if form.is_valid():
         form.save()
         return redirect('../../categorie/categorie')
   context={'form':form}
   return render(request,'categorie/ajouter_cat.html',context)



def modifier_categorie(request,pk):
    Categorie=categorie.objects.get(id=pk)
    form = categorieform(instance=Categorie)
    if request.method == 'POST':
        form = categorieform(request.POST,instance=Categorie)
        if form.is_valid():
            form.save()
            return redirect('../../categorie/categorie')
    context = {'form': form}
    return render(request,'categorie/ajouter_cat.html',context)


def supprimer_categorie(request,pk):
    Categorie=categorie.objects.get(id=pk)
    if request.method=='POST':
        Categorie.delete()
        return redirect('../../categorie/categorie')
    context={'item':Categorie}
    return render(request,'categorie/supprimer_categorie.html',context)