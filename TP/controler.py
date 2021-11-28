from model import *


def nourrir(animal_id):
    animals = open_files()[0]

    if animal_id in animals.keys():
        if verifie_disponibilite('mangeoire') == 'occupé':
            return "Désolé, la mangeoire est déjà occupée."

        if lit_etat(animal_id) != 'affamé':
            return "Désolé, " + str(animal_id) + " n'est pas affamé, il ne peut pas être nourri."

        if verifie_disponibilite('mangeoire') == 'libre' and lit_etat(animal_id) == 'affamé':
            change_lieu(animal_id, 'mangeoire')
            change_etat(animal_id, 'repus')
            return "Félicitations, " + str(animal_id) + " est dans la mangeoire et est repus !"



def divertir(animal_id):
    animals = open_files()[0]

    if animal_id in animals.keys():
        if verifie_disponibilite('roue') == 'occupé':
            return "Désolé, la roue est déjà occupée."

        if lit_etat(animal_id) != 'repus':
            return "Désolé, " + str(animal_id) + " ne se sent pas de courir pour le moment."

        if verifie_disponibilite('roue') == 'libre' and lit_etat(animal_id) == 'repus':
            change_lieu(animal_id, 'roue')
            change_etat(animal_id, 'fatigué')
            return "Félicitations, " + str(animal_id) + " est dans la roue et est fatigué !"

def coucher(animal_id):
    animals = open_files()[0]

    if animal_id in animals.keys():
        if verifie_disponibilite('nid') == 'occupé':
            return "Désolé, le nid est déjà occupé."

        if lit_etat(animal_id) != 'fatigué':
            return "Désolé, " + str(animal_id) + " ne se sent pas d'aller dormir."

        if verifie_disponibilite('nid') == 'libre' and lit_etat(animal_id) == 'fatigué':
            change_lieu(animal_id, 'nid')
            change_etat(animal_id, 'endormi')
            return "Félicitations, " + str(animal_id) + " est endormi dans le lit !"

def reveiller(animal_id):
    animals = open_files()[0]

    if animal_id in animals.keys():
        if lit_etat(animal_id) != 'endormi':
            return "Désolé, " + str(animal_id) + " ne dort pas."

        if lit_etat(animal_id) == 'endormi':
            change_lieu(animal_id, 'litière')
            change_etat(animal_id, 'affamé')
            return "Félicitations, " + str(animal_id) + " est affamé dans la litière !"




