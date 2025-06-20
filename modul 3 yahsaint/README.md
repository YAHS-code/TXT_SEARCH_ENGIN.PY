

 search_core.py
Ce module Python permet d’effectuer des recherches de mots dans un corpus de texte indexé. Il est conçu pour être simple à utiliser et facilement intégrable dans un projet d’analyse de texte.

 Fonctionnalités
 Recherche simple : retrouve toutes les occurrences d’un mot.

Recherche multiple : cherche plusieurs mots avec les modes OU (au moins un mot) ou ET (tous les mots).

Recherche par motif : utilise des expressions régulières (avec * comme joker).

 Description des fonctions
Fonction	Description
rechercher_mot(index, mot)	Retourne toutes les occurrences du mot donné.
recherche_multiple(index, mots, mode='OU')	Cherche plusieurs mots dans l’index. Deux modes : OU pour élargir, ET pour affiner.
recherche_regex(index, motif)	Recherche tous les mots correspondant au motif (supporte le *). Affiche les résultats groupés par mot trouvé.
Pré-requis
L’index doit être un dictionnaire avec des mots comme clés, et pour chaque mot une liste de dictionnaires contenant :

fichier : le nom du fichier,

ligne : le numéro de ligne,

position : la position du mot dans la ligne.

Exemple de structure d’index
python
{
  "python": [
    {"fichier": "doc1.txt", "ligne": 3, "position": 15},
    {"fichier": "doc2.txt", "ligne": 1, "position": 8}
  ]
}