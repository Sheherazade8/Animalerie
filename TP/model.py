import json


def open_files():
    return json.loads(open('animal.json', 'r+').read()), json.loads(open('equipment.json', 'r+').read())


def lit_etat(animal_id):
    animals = open_files()[0]

    if animal_id in animals.keys():
        return animals[animal_id]['ETAT']
    else:
        print("Cet animal n'est pas dans l'animalerie.")
        return None


def lit_lieu(animal_id):
    animals = open_files()[0]

    if animal_id in animals.keys():
        return animals[animal_id]['LIEU']
    else:
        print("Cet animal n'est pas dans l'animalerie.")
        return None


def verifie_disponibilite(equipment_id):
    equipment = open_files()[1]

    if equipment_id in equipment.keys():
        return equipment[equipment_id]['DISPONIBILITÉ']
    else:
        print("Ce lieu n'est pas dans l'animalerie.")
        return None


def cherche_occupant(lieu):
    animals = open_files()[0]
    equipment = open_files()[1]

    occupants = []

    if lieu in equipment.keys():

        for animal in animals.keys():
            if animals[animal]['LIEU'] == lieu:
                occupants.append(animal)

        else:
            return occupants
    else:
        print("Ce lieu n'est pas dans l'animalerie.")
        return None


def change_etat(id_animal, etat):
    animals = open_files()[0]

    if etat in ['affamé', 'fatigué', 'repus', 'endormi'] and lit_etat(id_animal):
        animals[id_animal]['ETAT'] = etat
        with open('animal.json', 'w') as file:
            json.dump(animals, file, indent=2)


def change_lieu(id_animal, lieu):
    animals = open_files()[0]
    equipment = open_files()[1]

    if id_animal in animals.keys():  # Passe change_lieu_nul(1)

        ancien_lieu = animals[id_animal]['LIEU']

        if lieu in equipment.keys():  # Passe change lieu_nul_(2)

            if lieu != 'litière':  # Vérifie la condition que la litière peut accueillir plusieurs animaux

                if equipment[lieu]['DISPONIBILITÉ'] == 'libre':  # Passe test_change_lieu_occupé

                    animals[id_animal]['LIEU'] = lieu  # On change le lieu de l'animal

                    with open('animal.json', 'w') as file:
                        json.dump(animals, file, indent=2)

                    equipment[lieu]['DISPONIBILITÉ'] = 'occupé'  # On change le statut du nouveau lieu de l'animal
                    equipment[ancien_lieu]['DISPONIBILITÉ'] = 'libre'  # On change le statut de l'ancien lieu de animal

                    with open('equipment.json', 'w') as file:
                        json.dump(equipment, file, indent=2)

                else:
                    print('Ce lieu est déjà occupé.')

            else:
                animals[id_animal]['LIEU'] = lieu

                with open('animal.json', 'w') as file:
                    json.dump(animals, file, indent=2)

                equipment[ancien_lieu]['DISPONIBILITÉ'] = 'libre'

                with open('equipment.json', 'w') as file:
                    json.dump(equipment, file, indent=2)
        else:
            print('Le lieu', lieu, "n'est pas dans l'animalerie.")
    else:
        print("L'animal nommé", id_animal, "n'est pas dans l'animalerie.")