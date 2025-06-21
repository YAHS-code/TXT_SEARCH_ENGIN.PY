import os
import re

# Fonction pour récupérer tous les fichiers .txt d'un dossier
def lire_fichiers(dossier):
    fichiers_txt = []
    if not os.path.exists(dossier):
        raise FileNotFoundError(f"Le dossier '{dossier}' spécifié n'existe pas.")
    if not os.path.isdir(dossier):
        raise NotADirectoryError(f"Le chemin '{dossier}' n'est pas un dossier.")

    for fichier in os.listdir(dossier):
        if fichier.endswith(".txt"):
            fichiers_txt.append(os.path.join(dossier, fichier))
    if not fichiers_txt:
        raise FileNotFoundError("Aucun fichier .txt trouvé dans le dossier spécifié.")
    return fichiers_txt

# Nettoyage d'une ligne : mise en minuscules + suppression ponctuation
def nettoyer_texte(ligne):
    ligne = ligne.lower()
    ligne = re.sub(r'[^a-z0-9\s]', '', ligne)
    return ligne

# Nouvelle fonction : lit et nettoie tout le contenu des fichiers
def lire_fichiers_et_nettoyer(dossier):
    fichiers = lire_fichiers(dossier)
    resultats = {}

    for chemin in fichiers:
        with open(chemin, 'r', encoding='utf-8') as f:
            lignes_nettoyees = [nettoyer_texte(ligne.strip()) for ligne in f if ligne.strip()]
            resultats[os.path.basename(chemin)] = lignes_nettoyees

    return resultats
