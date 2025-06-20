from collections import Counter

# Fonction pour extraire des statistiques à partir de l'index
def stats_index(index):
    stats = {}
    fichiers = Counter()
    mot_frequences = Counter()
    for mot, entrees in index.items():
        mot_frequences[mot] += len(entrees)
        for entree in entrees:
            fichiers[entree['fichier']] += 1
    stats['Nombre total de fichiers analysés'] = len(fichiers)
    stats['Nombre de mots uniques indexés'] = len(index)
    stats['🔝 Top 10 des mots les plus fréquents'] = mot_frequences.most_common(10)
    stats['📁 Fichiers contenant le plus de mots'] = fichiers.most_common(3)
    return stats

# Export des résultats dans un fichier texte simple
def exporter_resultats(resultats, chemin='resultats.txt'):
    with open(chemin, 'w', encoding='utf-8') as f:
        for r in resultats:
            f.write(f"{r['fichier']} - ligne {r['ligne']} - position {r['position']}\n")

