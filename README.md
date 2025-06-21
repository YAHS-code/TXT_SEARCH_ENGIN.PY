 Projet 9 – Moteur de recherche dans des fichiers .txt (TXT_SEARCH_ENGINE.PY)

##  Description du projet

Ce projet vise à développer un *moteur de recherche* en Python capable d'analyser un dossier contenant des fichiers .txt, d’*indexer automatiquement tous les mots, et de permettre à l’utilisateur de **rechercher des mots-clés* pour localiser :
- les *fichiers concernés*,
- les *lignes où le mot apparaît*, 
- et la *position du mot dans chaque ligne*.

Un système d’index est généré et sauvegardé au format JSON pour être réutilisé sans recharger tous les fichiers à chaque lancement.

##  Fonctionnalités principales

-  Lecture automatique de fichiers .txt dans un dossier (ex. data/)
   Nettoyage du texte : suppression des ponctuations, conversion en minuscules
-  Indexation des mots : fichier, numéro de ligne, et position dans la ligne
-  Sauvegarde & chargement de l’index au format index.json
-  Recherche par mot-clé simple
-  Recherche multiple :
  - OU : mot A *ou* mot B
  - ET : mot A *et* mot B
-  Recherche avec expressions régulières (ex: prog.*)
-  Statistiques sur les fichiers indexés :
  - nombre de fichiers
  - nombre de mots uniques
  - top 10 des mots les plus fréquents
  - fichiers les plus riches
  - occurrences de chaque mot
-  (Bonus) Export des résultats de recherche au format .txt ou .csv
-  Gestion des erreurs (dossier inexistant, vide, pas de .txt, etc.)

---

##  Architecture modulaire

Le projet est organisé en *5 modules* pour un travail d’équipe fluide :

###  Module 1 : file_reader.py – Lecteur de fichiers & nettoyage
- Explorer un dossier (data/) et lire tous les fichiers .txt
- Nettoyer le texte (minuscules, suppression ponctuation)
- Gérer les erreurs de lecture (dossier inexistant, vide)
- Utilisation des modules : os, re

###  Module 2 : word_indexer.py – Indexeur de mots
- Construire un index : {mot: [{fichier, ligne, position}, ...]}
- Sauvegarde et chargement de index.json
- Utilisation des structures de données et module json

###  Module 3 : search_core.py – Moteur de recherche
- Recherche d’un mot simple dans l’index
- Recherche multiple (OU / ET)
- Recherche par expression régulière (avec re)
- Fusion, intersection et filtrage des résultats

###  Module 4 : stats_analyzer.py – Statistiques & export
- Calcul :
  - nombre de fichiers indexés
  - total de mots uniques
  - top 10 mots fréquents
  - fichiers les plus riches
  - fréquence de chaque mot
- Export des résultats (.txt ou .csv)
- Utilisation de csv, tri de dictionnaires, agrégation

###  Module 5 : main_cli.py – Interface utilisateur CLI
- Menu interactif pour :
  - choisir un dossier
  - entrer un mot ou une expression
  - sélectionner une option de recherche (mot simple, OU, ET, regex)
  - afficher les résultats ou les statistiques
- Coordination avec les autres modules
- Utilisation de argparse ou menu manuel CLI

---

##  Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/txt_search_engine.git
   cd txt_search_engine

2. Installer les dépendances (Python ≥ 3.8) :

pip install -r requirements.txt


3. Créer un dossier data/ à la racine et y placer des fichiers .txt.




 Utilisation

Lancer l’interface utilisateur :

python main_cli.py

Exemples de commandes possibles :

Rechercher un mot simple → programmation

Rechercher avec logique OU → python java (mode OU)

Rechercher avec logique ET → python java (mode ET)

Rechercher par regex → prog.*

Consulter les statistiques

Exporter les résultats



 Exemple d'index (index.json)

{
  "python": [
    {
      "fichier": "intro.txt",
      "ligne": 2,
      "position": 5
    },
    {
      "fichier": "tutoriel.txt",
      "ligne": 1,
      "position": 8
    }
  ]
}


 Gestion des erreurs

 Dossier data/ inexistant → message d’erreur clair

 Aucun fichier .txt trouvé → avertissement

 Fichiers illisibles → erreur gérée

 Recherche de mots absents → message : "Aucune occurrence trouvée"



Bonus

Exporter les résultats de recherche en .txt ou .csv via l’interface CLI

Peut être intégré dans une future interface graphique (ex: Tkinter)



Équipe

Nom	Module	Rôle

Étudiant 1	file_reader.py	Lecture de fichiers & nettoyage
Étudiant 2	word_indexer.py	Construction & sauvegarde de l’index
Étudiant 3	search_core.py	Recherche simple, multiple, regex
Étudiant 4	stats_analyzer.py	Statistiques & export
Étudiant 5	main_cli.py	Interface CLI & coordination



 À noter

Bien séparer le code en modules clairs.

Documenter chaque fonction (docstrings).

Tester sur plusieurs fichiers .txt variés.

Optimiser les performances si les fichiers sont très grands.

