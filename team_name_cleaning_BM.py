import pandas as pd
import re
from fuzzywuzzy import fuzz

def clean_name(name):
   
    suffixes = r'\s*(FC|Club|SFC|SPFC|RET|Bait Jair|Sports Club|Sporting|Mohammedein FC)$'
    cleaned = re.sub(suffixes, '', str(name), flags=re.IGNORECASE)
    return cleaned.lower().strip()


def standardize_team_names(df):
    # On récupère tous les noms d'équipes
    all_team_names = []
    for col in ['provider_1_team_name', 'provider_2_team_name', 'provider_3_team_name']:
        for name in df[col].dropna().unique():
            if name not in all_team_names:  # Évite les doublons
                all_team_names.append(name)
    
    # On prépare une liste pour stocker nos groupes d'équipes
    clusters = []
    
    SEUIL_SIMILARITE = 85 
    
    # On va traiter chaque nom un par un
    for name in all_team_names:
        trouve = False
        
        # On nettoie le nom  
        cleaned_name = clean_name(name)
        
        # On cherche si ça matche avec un groupe existant
        for cluster in clusters:
            # On prend le premier nom du groupe comme référence
            ref_name = cluster[0]
            cleaned_ref = clean_name(ref_name)
            
            # Calcul de la similarité avec fuzzy
            score = fuzz.partial_ratio(cleaned_name, cleaned_ref)
            
            if score > SEUIL_SIMILARITE:
                cluster.append(name)
                trouve = True
                break
        
        # Si on a rien trouvé, on crée un nouveau groupe
        if not trouve:
            clusters.append([name])
    
    # Maintenant on crée le mapping pour la standardisation
    name_mapping = {}
    for cluster in clusters:
        # On choisit le nom le plus long comme standard souvent le plus complet
        standard = max(cluster, key=len)
        
        # On ajoute chaque variante au mapping
        for variant in cluster:
            name_mapping[variant] = standard
    
    return name_mapping


def main():
    df = pd.read_excel('data/file_ASM.xlsx', sheet_name='club_names_ids')
    
    name_mapping = standardize_team_names(df)
    print(name_mapping)
    print("____________________________________________________________________")
    # Appliquer le mapping
    df['standard_team_name'] = df['provider_1_team_name'].map(name_mapping)
    
    # Sauvegarder le résultat
    df.to_excel('cleaned_teams_BM.xlsx', index=False)
    print("Standardisation terminée. Résultats sauvegardés dans 'cleaned_teams_BM.xlsx'")

if __name__ == "__main__":
    main()