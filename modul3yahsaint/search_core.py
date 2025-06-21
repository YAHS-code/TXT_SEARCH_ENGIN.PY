# search_core.py
import re
from collections import defaultdict

# Recherche simple : retourne les occurrences d'un mot
def rechercher_mot(index, mot):
    mot = mot.lower()
    return index.get(mot, [])

# Recherche multiple : mode OU (union) ou ET (intersection)
def recherche_multiple(index, mots, mode='OU'):
    mots = [mot.lower() for mot in mots]
    resultats = []

    if mode == 'OU':
        for mot in mots:
            resultats.extend(index.get(mot, []))

    elif mode == 'ET':
        # Récupérer les ensembles de fichiers pour chaque mot
        fichiers_par_mot = [set(entry['fichier'] for entry in index.get(mot, [])) for mot in mots]
        if fichiers_par_mot:
            # Intersecter les fichiers pour trouver ceux contenant tous les mots
            fichiers_communs = set.intersection(*fichiers_par_mot)
            # Récupérer toutes les occurrences dans ces fichiers
            for mot in mots:
                for occ in index.get(mot, []):
                    if occ['fichier'] in fichiers_communs:
                        resultats.append(occ)

    return resultats

# Recherche avec une expression régulière sur les mots de l'index
def recherche_regex(index, motif):
    # Remplace les caractères joker * par .* pour correspondre à n'importe quelle séquence
    motif = motif.replace("*", ".*")
    pattern = re.compile(motif)
    resultats = []
    mots_resultats = defaultdict(list)

    for mot in index:
        if pattern.fullmatch(mot):
            for occurence in index[mot]:
                occurence_avec_mot = occurence.copy()
                occurence_avec_mot['mot'] = mot
                resultats.append(occurence_avec_mot)
                mots_resultats[mot].append(occurence)

    if resultats:
        print("\nRésultats de recherche (groupés par mot trouvé) :")
        for mot in sorted(mots_resultats.keys()):
            print(f"\nMot : {mot}")
            for occ in mots_resultats[mot]:
                print(f" - Fichier : {occ['fichier']}, Ligne : {occ['ligne']}, Position : {occ['position']}")
    else:
        print("\nAucun mot trouvé pour ce motif.")

    return resultats
