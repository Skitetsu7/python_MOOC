# mutant_generator.py
import random
import copy

# Liste de mots pour les mutants
mots_base = ['pomme', 'banane', 'orange']

# Mutations possibles
def mutate_vie(vie):
    """Mutation: change la vie initiale"""
    return vie + 1  # dépassement volontaire

def mutate_mot(mot):
    """Mutation: toujours le premier mot"""
    return mots_base[0]

def mutate_win_or_lose(words, letter):
    """Mutation: retourne toujours 1"""
    return 1

def mutate_demande_lettre():
    """Mutation: toujours retourne 'a'"""
    return 'a'

# Jeu de base à muter
def jeu_running(vie=6, choisir_mot_func=None, demande_lettre_func=None, win_or_lose_func=None):
    if choisir_mot_func is None:
        choisir_mot_func = lambda: random.choice(mots_base)
    if demande_lettre_func is None:
        demande_lettre_func = lambda: input("Entrez une lettre: ")
    if win_or_lose_func is None:
        win_or_lose_func = lambda mot, lettre: lettre in mot

    mot = choisir_mot_func()
    lettre_trouvee = []
    lettre_fausse = []

    while vie != 0 and len(lettre_trouvee) != len(set(mot)):
        print("Mot:", ''.join(l if l in lettre_trouvee else '_' for l in mot))
        lettre = demande_lettre_func()

        if win_or_lose_func(mot, lettre) and lettre not in lettre_trouvee:
            lettre_trouvee.append(lettre)
        else:
            if lettre not in lettre_fausse:
                vie -= 1
                lettre_fausse.append(lettre)
        print("Vies:", vie)

    if len(lettre_trouvee) == len(set(mot)):
        print("Victoire! Mot:", mot)
    else:
        print("Défaite! Mot:", mot)

# Liste des mutants
mutants = [
    {"vie": mutate_vie, "choisir_mot": None, "demande_lettre": None, "win_or_lose": None},
    {"vie": 6, "choisir_mot": mutate_mot, "demande_lettre": None, "win_or_lose": None},
    {"vie": 6, "choisir_mot": None, "demande_lettre": mutate_demande_lettre, "win_or_lose": None},
    {"vie": 6, "choisir_mot": None, "demande_lettre": None, "win_or_lose": mutate_win_or_lose},
]

# Exécution des mutants
for i, m in enumerate(mutants):
    print(f"\n=== Exécution du mutant {i+1} ===")
    vie = m 
    jeu_running(
        vie=vie,
        choisir_mot_func=m["choisir_mot"],
        demande_lettre_func=m["demande_lettre"],
        win_or_lose_func=m["win_or_lose"]
    )
