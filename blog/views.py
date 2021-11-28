
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Animal, Equipement



def animal_list(request):
    animals = Animal.objects.filter()
    return render(request, 'blog/post_list.html', {'animals': animals})


def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
    form = MoveForm(request.POST, instance=animal)
    if form.is_valid():
        form.save(commit=False)
        if animal.lieu.disponibilite == "libre" or animal.lieu.id_equip == "Litière":
            animal.save()
            #nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
            if ancien_lieu.id_equip != "Litière":
                ancien_lieu.disponibilite = "libre"
                ancien_lieu.save()
            animal.lieu.disponibilite = "occupé"
            animal.save()
            if animal.lieu.id_equip == "Nid":
                animal.etat = "endormi"
            elif animal.lieu.id_equip == "Litière":
                animal.etat = "affamé"
                animal.etat = "affamé"
            elif animal.lieu.id_equip == "Mangeoire":
                animal.etat = "repus"
            elif animal.lieu.id_equip == "Roue":
                animal.etat = "fatigué"
            animal.save()
            return redirect('animal_detail', id_animal=id_animal)
        else :
            animal.lieu = ancien_lieu
            animal.save()
            return render(request,
                          'blog/animal_detail.html',
                          {'animal': animal, 'lieu': animal.lieu, 'form': form, 'message' : "le lieu indiqué n'est pas disponible"})
    else:
        form = MoveForm()
        return render(request,
                  'blog/animal_detail.html',
                  {'animal': animal, 'lieu': animal.lieu, 'form': form, 'message' : 'indiquer un lieu'})