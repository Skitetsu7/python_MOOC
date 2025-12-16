# python_MOOC

le problème dans le code c'est l'appel du jeu du coup faut : 
if __name__ == "__main__":
    jeu = 1
    while jeu:
        jeu_running()
        jeu = rejouer()

aussi il y a un warning:
Python considère \o comme un caractère d’échappement invalide.
Pour corriger, faut soit doubler le backslash \\o ou soit utiliser des raw strings :

print(r" ___ \n | | \n |\o/ \n | | \n |/ \ \n---")
