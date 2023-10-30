from django.shortcuts import render,redirect
from sous_categorie.models import sous_categorie
from .forms import materielform
from .models import materiel
# Create your views here.
def Materiel(request):
   Sous_cat = sous_categorie.objects.all()
   Materiel = materiel.objects.all()
   souscat_found = "rien"
   for s in Sous_cat:
      if s.id == int(request.GET.get('id')):
         souscat_found = s
         break
   liste_mat = []
   for m in Materiel:
      if m.Type == souscat_found:
         liste_mat.append(m)
   context = {'liste_mat': liste_mat, 'souscat_found': souscat_found, 'Sous_cat': Sous_cat, 'Materiel': Materiel}
   return render(request, 'materiel/materiel.html', context)




def ajouter_materiel(request):
   form=materielform()
   if request.method=='POST':
       form=materielform(request.POST)
       if form.is_valid():
         form.save()
         return redirect('../../categorie/categorie')
   context={'form':form}
   return render(request,'materiel/ajouter_mat.html',context)


def modifier_materiel(request, pk):
   Materiel = materiel.objects.get(id=pk)
   form = materielform(instance=Materiel)
   if request.method == 'POST':
      form = materielform(request.POST, instance=Materiel)
      if form.is_valid():
         form.save()
         return redirect('../../categorie/categorie')
   context = {'form': form}
   return render(request, 'materiel/ajouter_mat.html', context)


def supprimer_materiel(request, pk):
   Materiel = materiel.objects.get(id=pk)
   if request.method == 'POST':
      Materiel.delete()
      return redirect('../../categorie/categorie')
   context = {'item': Materiel}
   return render(request, 'materiel/supprimer_mat.html', context)


def afficher_mat(request):
   Mat = materiel.objects.all()
   context = {'Mat': Mat}
   return render(request, 'materiel/afficher_mat.html', context)
