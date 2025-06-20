import os
import re

# Fonction pour récupérer tous les fichiers .txt d'un dossier
# Renvoie une liste des chemins complets des fichiers .txt
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

# Fonction pour nettoyer une ligne de texte : minuscules + suppression ponctuation
# Seuls les chiffres, lettres et espaces sont conservés
def nettoyer_texte(ligne):
    ligne = ligne.lower()
    ligne = re.sub(r'[^a-z0-9\s]', '', ligne)
    return ligne

