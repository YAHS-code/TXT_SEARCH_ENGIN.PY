📚 Indexeur de Mots dans des Fichiers Texte
Ce projet est un outil Python simple qui parcourt un dossier contenant des fichiers texte, analyse leur contenu, et crée un index des mots. Pour chaque mot, l'index indique dans quel fichier il se trouve, à quelle ligne, et à quelle position dans la ligne.

🚀 Fonctionnalités
Lecture automatique des fichiers texte d'un dossier

Nettoyage du contenu texte (via nettoyer_texte)

Indexation des mots avec :

Le nom du fichier

Le numéro de ligne

La position du mot dans la ligne

Sauvegarde de l'index au format JSON

Chargement d'un index existant si présent

🛠️ Fichiers et Fonctions Principales
creer_index(dossier) : crée l'index pour tous les fichiers du dossier

sauvegarder_index(index, chemin) : enregistre l'index dans un fichier JSON

charger_index(chemin) : charge l'index à partir d'un fichier JSON

file_reader.py : contient les fonctions lire_fichiers et nettoyer_texte

📂 Format de l'Index
json
{
  "mot": [
    {
      "fichier": "nom_du_fichier.txt",
      "ligne": 12,
      "position": 4
    },
    ...
  ]
}
✅ Prérequis
Python 3.x

Un fichier file_reader.py contenant les fonctions d'aide

📌 Exemple d'utilisation
python
index = creer_index("mes_fichiers")
sauvegarder_index(index)
🧹 Astuce
Assurez-vous que vos fichiers soient encodés en UTF-8 pour éviter les erreurs de lecture