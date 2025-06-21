import os
import json
import csv
from modul1Randy.file_reader import lire_fichiers_et_nettoyer
from modul2Ruth.word_indexer import creer_index, sauvegarder_index, charger_index
from modul3yahsaint.search_core import rechercher_mot, recherche_multiple, recherche_regex
from module4Naomie.stats_analyzer import calculer_statistiques, exporter_resultats as exporter_stats

def afficher_menu():
    print("\n=== MOTEUR DE RECHERCHE TXT ===")
    print("1. Indexer un dossier")
    print("2. Rechercher un mot")
    print("3. Rechercher plusieurs mots (OU / ET)")
    print("4. Rechercher par expression régulière")
    print("5. Afficher les statistiques")
    print("6. Exporter les résultats")
    print("0. Quitter")

def demander_chemin():
    chemin = input("Entrez le chemin du dossier contenant les fichiers .txt : ")
    if not os.path.exists(chemin):
        print("❌ Dossier non trouvé.")
        return None
    fichiers_txt = [f for f in os.listdir(chemin) if f.endswith(".txt")]
    if not fichiers_txt:
        print("❌ Aucun fichier .txt trouvé dans le dossier.")
        return None
    return chemin

def afficher_resultats(resultat):
    if not resultat:
        print("Aucun résultat trouvé.")
        return
    # resultat attendu : liste d'occurrences {fichier, ligne, position, mot?}
    for occ in resultat:
        mot = occ.get('mot', '')
        print(f"Mot : {mot} | Fichier : {occ['fichier']} | Ligne : {occ['ligne']} | Position : {occ['position']}")

def exporter_resultats(resultats, nom_fichier, format_):
    if format_ == 'txt':
        with open(f"{nom_fichier}.txt", 'w', encoding='utf-8') as f:
            for occ in resultats:
                mot = occ.get('mot', '')
                f.write(f"Mot : {mot} | Fichier : {occ['fichier']} | Ligne : {occ['ligne']} | Position : {occ['position']}\n")
    elif format_ == 'csv':
        with open(f"{nom_fichier}.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['mot', 'fichier', 'ligne', 'position'])
            writer.writeheader()
            for occ in resultats:
                writer.writerow({
                    'mot': occ.get('mot', ''),
                    'fichier': occ['fichier'],
                    'ligne': occ['ligne'],
                    'position': occ['position']
                })
    else:
        print("Format non supporté. Utilisez 'txt' ou 'csv'.")

def main():
    index = {}
    dernier_resultat = []

    if os.path.exists("index.json"):
        print("✅ Chargement de l'index existant...")
        index = charger_index("index.json")
    else:
        print("ℹ️ Aucun index trouvé. Veuillez indexer un dossier.")

    while True:
        afficher_menu()
        choix = input("Choix : ").strip()

        if choix == "1":
            chemin = demander_chemin()
            if chemin:
                print("📖 Lecture et nettoyage des fichiers...")
                fichiers_nettoyes = lire_fichiers_et_nettoyer(chemin)
                index = creer_index_dictionnaire(fichiers_nettoyes)  # cf fonction ci-dessous
                sauvegarder_index(index, "index.json")
                print("✅ Indexation terminée et sauvegardée.")

        elif choix == "2":
            mot = input("Mot à rechercher : ").lower()
            if index:
                resultat = rechercher_mot(index, mot)
                afficher_resultats(resultat)
                dernier_resultat = resultat
            else:
                print("❌ L'index est vide. Veuillez d'abord indexer un dossier.")

        elif choix == "3":
            mots = input("Entrez plusieurs mots séparés par un espace : ").lower().split()
            mode = input("Mode (OU/ET) : ").strip().upper()
            if index:
                resultat = recherche_multiple(index, mots, mode)
                afficher_resultats(resultat)
                dernier_resultat = resultat
            else:
                print("❌ L'index est vide.")

        elif choix == "4":
            pattern = input("Entrez l'expression régulière (ex: prog.*) : ").strip()
            if index:
                resultat = recherche_regex(index, pattern)
                afficher_resultats(resultat)
                dernier_resultat = resultat
            else:
                print("❌ L'index est vide.")

        elif choix == "5":
            if index:
                stats = calculer_statistiques(index)
                for cle, valeur in stats.items():
                    print(f"{cle} : {valeur}")
            else:
                print("❌ L'index est vide.")

        elif choix == "6":
            if dernier_resultat:
                format_ = input("Format d'export (txt/csv) : ").strip().lower()
                nom_fichier = input("Nom du fichier (sans extension) : ").strip()
                exporter_resultats(dernier_resultat, nom_fichier, format_)
                print("✅ Résultats exportés.")
            else:
                print("❌ Aucun résultat à exporter.")

        elif choix == "0":
            print("👋 Fin du programme.")
            break
        else:
            print("❌ Choix invalide.")

def creer_index_dictionnaire(docs_nettoyes):
    """
    docs_nettoyes : dict { nom_fichier: [lignes nettoyées] }
    Crée un index inversé (mot -> occurrences)
    """
    index = {}
    for nom_fichier, lignes in docs_nettoyes.items():
        for num_ligne, ligne in enumerate(lignes, 1):
            mots = ligne.split()
            for pos, mot in enumerate(mots):
                if mot not in index:
                    index[mot] = []
                index[mot].append({
                    'fichier': nom_fichier,
                    'ligne': num_ligne,
                    'position': pos
                })
    return index

if __name__ == "__main__":
    main()
