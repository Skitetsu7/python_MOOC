
# jeu du pendu
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
assert all(char in 'abcdefghijklmnopqrstuvwxyzàâäéèêëîïôöùûüç' for char in accent_letter.keys()), "les conditions de lettres minuscules doivent être respecter."

# Fonction pour choisir un mot au hasard
# avec un fichier au choix de l'utilisateur ou le fichier de base
def choisir_mot():
    print(
        '\nSi vous voulez utiliser un fichier texte personnel pour le jeu, \nAssurez-vous que le fichier contienne un '
        'mot par ligne séparé par un Entrée ')

    fiche = input('Entrez le nom du fichier .txt sinon pressez Entrée:')
    # assert isinstance(fiche, str), "le fichier doit être avec des caractere"
    # si le joueur veut utiliser un fichier personnel
    while fiche != '':
        # on regarde l'extension
        if not fiche.endswith('.txt'):
            print("Erreur : Le fichier doit avoir une extension .txt.")
        else:
            try: #oracle fort (plus précis)
                # assert fiche is not None #vérifie que le fichier n'est pas None
                with open(fiche, 'r') as fichier:
                    # assert fichier.readable(), "le fichier doit être lisible"
                    contenu = fichier.read()

                if contenu.strip():
                    # assert len(contenu) > 0, "le fichier ne doit pas être vide"
                    break
                else:
                    print(f"Le fichier '{fiche}' est vide. Assurez-vous qu'il contienne des mots.")
            except FileNotFoundError:
                print(f"[ERREUR] Fichier '{fiche}' introuvable.")
            except PermissionError:
                print(f"[ERREUR] Accès refusé au fichier '{fiche}'.")

    """ oracle faible : Objectif : ne jamais planter, quoi qu’il arrive.
try:
    with open(fiche, 'r') as fichier:
        contenu = fichier.read()

    if contenu.strip():
        break
    else:
        print(f"Le fichier '{fiche}' est vide. Assurez-vous qu'il contienne des mots.")
except FileNotFoundError:
    print(f"Fichier '{fiche}' introuvable. Veuillez réessayer.")
except Exception:
    print("Erreur inattendue lors de la lecture du fichier.")

        oracle logqique: Différencier erreur système / erreur de contenu.
try:
    with open(fiche, 'r') as fichier:
        contenu = fichier.read()

    assert contenu is not None

    if contenu.strip():
        break
    else:
        print(f"Le fichier '{fiche}' est vide. Assurez-vous qu'il contienne des mots.")
except FileNotFoundError:
    print(f"Fichier '{fiche}' introuvable. Veuillez réessayer.")

    
    """

    fiche = input('Entrez le nom du fichier .txt sinon pressez Entrée:')
    # si il a pressé entrée on utilise le fichier par défaut
    if fiche == '':
        fiche = 'mots_pendu.txt'

    # Ouverture du fichier en mode lecture
    with open(fiche, 'r') as fichier:
        contenu = fichier.read()
    # Création d'une liste de mots en éliminant les saut de ligne
    mots = contenu.split('\n')
    # mot final random
    mot = random.choice(mots)

    # passage de toutes les lettres en minuscule
    mot = mot.lower()
    return ''.join(accent_letter.get(char, char) for char in mot)


def demande_lettre():
    while True:
        lettre = input('Tapez une lettre minuscule :')
        if len(lettre) == 1 and lettre.isalpha() and lettre.islower():
            return lettre
        else:
            print("Veuillez entrer une seule lettre minuscule.")


# Fonction permettant l'affichage du nombre de vie et du pendu dans la console
def affichage_vie(vie):
    if vie == 6:
        print("Il vous reste 6 vies\n")
    if vie == 5:
        print("---")
        print("Il vous reste 5 vies\n")
    if vie == 4:
        print(" |\n | \n |\n |\n---")
        print("Il vous reste 4 vies\n")
    if vie == 3:
        print(" ___ \n | \n |\n |\n |\n---")
        print("Il vous reste 3 vies\n")
    if vie == 2:
        print(" ___ \n | | \n |\o/ \n |\n |\n---")
        print("Il vous reste 2 vies\n")
    if vie == 1:
        print(" ___ \n | | \n |\o/ \n | | \n |\n---")
        print("Il vous reste 1 vie \n")
    if vie == 0:
        print(" ___ \n | | \n |\o/ \n | | \n |/ \ \n---")
        print("Vous n'avez plus de vie, DEFAITE \n")

# Fonction pour afficher le mot en fonction des lettres trouvées
# words et le mot désigné par le jeu et nblettre une liste des lettres trouvées par le joueur
def affichage_mot(mot, nblettre):
    mot_affiche = ['_' if lettre not in nblettre else lettre for lettre in mot]
    print(' '.join(mot_affiche))


# on vérifie si la lettre donnée appartient au mot du jeu
# on renvoie 1 si elle appartient 0 sinon
# de plus si la lettre donnée à un accent on la remplace par la lettre sans  accent
def win_or_lose(words, letter):
    letter = accent_letter.get(letter, letter)
    for i in range(len(words)):
        if letter == words[i]:
            return 1
    return 0


# fonction pour donner un indice
def indice(lettres_tapees, mot):
    # listes des lettres de l'alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # on enlève les lettres déjà tapées
    lettres_disponibles = [lettre for lettre in alphabet if lettre not in lettres_tapees]

    # on enlève les lettres présentes dans le mot
    lettres_disponibles = [lettre for lettre in lettres_disponibles if lettre not in mot]

    # on prend une lettre aléatoire parmi les lettres disponibles
    if lettres_disponibles:
        lettre_indice = random.choice(lettres_disponibles)
        print(f"Indice : La lettre '{lettre_indice}' n'est pas dans le mot.")


# fonction de jeu prennant en compte les fonctions précédentes
def jeu_running():
    mot = choisir_mot()
    vie = 6
    lettre_trouvee = []
    lettre_fausse = []
    
    
    assert vie<= 6 # le joueur ne pas exceder 6 vies
    assert all(c.isalpha() for c in mot) #le mot doit ne poceder que des lettres

    print("Vie:", vie)
    print("Lettres trouvées:", lettre_trouvee)
    print("Mot:", mot)

    # on joue tant que le joueur a pas 0 vie et que le mot n'est pas trouvé
    # on doit comparer les lettres trouvées au nombre de lettres différentes dans le mot
    while vie != 0 and len(lettre_trouvee) != len(set(mot)):
        print(vie)
        print(len(lettre_trouvee))
        affichage_mot(mot, lettre_trouvee)
        lettre = demande_lettre()

        # on regarde si la lettre appartien au mot
        # si oui on ajoute à la liste des lettres trovuées
        # sinon on enlève une vie
        if win_or_lose(mot, lettre) and lettre not in lettre_trouvee:
            lettre_trouvee.append(lettre)
            print('La lettre tapée appartient bien au mot secret!\n')
        else:
            # Vérifie si la lettre n'est pas déjà dans la liste des lettres fausses
            if lettre not in lettre_fausse:
                assert vie > 0 # assertion 
                vie -= 1
                lettre_fausse.append(lettre)
                
        assert vie >= 0
        assert vie <= 6
        assert len(lettre_trouvee) <= len(set(mot))
        assert all(len(l)==1 for l in lettre_trouvee)

        affichage_vie(vie)
        # si il reste qu'une vie on donne un indice
        if vie == 1:
            indice(lettre_fausse, mot)
    # si le joueur a trouvé le mot
    assert len(lettre_trouvee)<= len(set(mot))
    if len(lettre_trouvee) == len(set(mot)):
        print('Victoire, vous avez trouvé le mot qui était :', mot)


# fonction pour demander au joeur si il veut rejouer ou quitter
def rejouer():
    while True:
        again = input('La partie est terminée, tapez 1 pour rejouer, 0 sinon : ')
        if again not in ('0', '1'):
            print("Entrée invalide.")
            print("Veuillez entrer 0 ou 1.")
        else:
            return int(again)


#############################################
# Gestion du jeu avec les fonctions précédentes
if __name__ == "__main__":
    jeu = 1
    while jeu:
        jeu_running()
        jeu = rejouer()

