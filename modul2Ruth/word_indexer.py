import os
import json
from modul1Randy.file_reader import lire_fichiers, nettoyer_texte

# Fonction principale pour créer un index inversé des mots
# Chaque mot est associé à une liste d’occurrences (fichier, ligne, position)
def creer_index(dossier):
    index = {}
    fichiers = lire_fichiers(dossier)
    
    for fichier in fichiers:
        with open(fichier, 'r', encoding='utf-8') as f:
            for num_ligne, ligne in enumerate(f, 1):
                ligne_nettoyee = nettoyer_texte(ligne)
                mots = ligne_nettoyee.split()
                for pos, mot in enumerate(mots):
                    if mot not in index:
                        index[mot] = []
                    index[mot].append({
                        'fichier': os.path.basename(fichier),
                        'ligne': num_ligne,
                        'position': pos
                    })
    
    return index

# Sauvegarde de l'index dans un fichier JSON
def sauvegarder_index(index, chemin='index.json'):
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)

# Chargement d’un index depuis un fichier JSON, si présent
def charger_index(chemin='index.json'):
    if os.path.exists(chemin):
        with open(chemin, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None
