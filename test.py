import json

def ecrire_dans_fichier(data, nom_fichier):
    try:
        with open(nom_fichier, 'w') as fichier:
            json.dump(data, fichier, indent=4)
        print(f"Données écrites dans le fichier {nom_fichier}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
donnees = {"cle1": "valeur1", "cle2": "valeur2"}

# Écriture des données dans le fichier (écrasera le contenu s'il existe déjà)
ecrire_dans_fichier(donnees, "./save/save.json")
