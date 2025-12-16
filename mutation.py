# jeu du pendu muté
import random

# Pour gérer les lettres avec accents
accent_letter = {
    'à': 'a', 'â': 'a', 'ä': 'a',
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'î': 'i', 'ï': 'i',
    'ô': 'o', 'ö': 'o',
    'ù': 'u', 'û': 'u', 'ü': 'u',
    'ç': 'c'
}

# Fonction pour choisir un mot au hasard (mutation: mot fixé au lieu de random)
def choisir_mot_mutant():
    mots = ['pomme', 'banane', 'orange']
    # Mutation: on ne choisit jamais aléatoirement, prend toujours le premier
    mot = mots[0]  
    mot = mot.lower()
    return ''.join(accent_letter.get(char, char) for char in mot)

# Fonction pour demander une lettre (mutation: toujours retourne 'a')
def demande_lettre_mutant():
    return 'a'

# Affichage vie (reste inchangé)
def affichage_vie(vie):
    print(f"Vies restantes (mutant): {vie}")

# Affichage mot
def affichage_mot(mot, nblettre):
    mot_affiche = ['_' if lettre not in nblettre else lettre for lettre in mot]
    print(' '.join(mot_affiche))

# Mutation: win_or_lose retourne toujours 1 (ne détecte jamais faux)
def win_or_lose_mutant(words, letter):
    return 1  # mutant: ignore la vraie vérification

# Jeu principal avec mutants
def jeu_running_mutant():
    mot = choisir_mot_mutant()
    vie = 7  # mutant: vie initiale incorrecte
    lettre_trouvee = []
    lettre_fausse = []

    while vie != 0 and len(lettre_trouvee) != len(set(mot)):
        affichage_mot(mot, lettre_trouvee)
        lettre = demande_lettre_mutant()

        if win_or_lose_mutant(mot, lettre) and lettre not in lettre_trouvee:
            lettre_trouvee.append(lettre)
        else:
            if lettre not in lettre_fausse:
                vie -= 1
                lettre_fausse.append(lettre)

        affichage_vie(vie)

    if len(lettre_trouvee) == len(set(mot)):
        print('Victoire (mutant)! Mot:', mot)
    else:
        print('Défaite (mutant). Mot:', mot)

# Lancer le jeu mutant
if __name__ == "__main__":
    jeu_running_mutant()
