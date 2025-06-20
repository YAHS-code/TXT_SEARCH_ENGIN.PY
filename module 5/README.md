markdown
# 🧠 Moteur de Recherche TXT - CLI

Une application Python en ligne de commande permettant de créer un index de fichiers `.txt`, d'effectuer des recherches simples, multiples ou par expression régulière, et d'afficher ou exporter des statistiques.

## 🚀 Fonctionnalités

- 📁 Indexation automatique d'un dossier de fichiers `.txt`
- 🔍 Recherche de mots avec affichage des fichiers, lignes et positions
- 🧩 Recherche multiple avec opérateurs `OU` et `ET`
- 🔠 Recherche par expression régulière (regex)
- 📊 Statistiques : mots les plus fréquents, nombre de fichiers, etc.
- 💾 Export des résultats de recherche dans un fichier `resultats.txt`

## 🛠️ Installation

1. Clone ce dépôt :
   ```bash
   git clone https://github.com/ton-profil/moteur-recherche-cli.git
   cd moteur-recherche-cli
Assure-toi d'avoir Python 3.x installé.

Place tes fichiers .txt dans un dossier accessible.

🖥️ Utilisation
Lance simplement l'application avec :

bash
python main.py
Tu seras guidé à travers un menu interactif dans le terminal.

 Structure du Projet
main.py – Interface principale et boucle de menu

word_indexer.py – Indexation et gestion de l'index

search_core.py – Fonctions de recherche

stats_analyzer.py – Calculs statistiques et export

 Licences
Distribué sous la licence MIT. Voir LICENSE.md pour plus d’informations.

 Bonnes recherches !


Tu veux que je t’aide à générer aussi un `requirements.txt` ou une version anglaise ?