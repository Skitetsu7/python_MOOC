PS C:\Users\El familia\OneDrive\mp3> python -m pytest test_assertion.py
=========================== test session starts ===========================
platform win32 -- Python 3.9.0, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\El familia\OneDrive\mp3
collected 0 items / 1 error                                                

================================= ERRORS ==================================
___________________ ERROR collecting test_assertion.py ____________________ 
test_assertion.py:2: in <module>
    import pendu_game
pendu_game.py:229: in <module>
    jeu_running()
pendu_game.py:165: in jeu_running
    mot = choisir_mot()
pendu_game.py:23: in choisir_mot
    fiche = input('Entrez le nom du fichier .txt sinon pressez Entrée:')    
C:\Python\Python39\lib\site-packages\_pytest\capture.py:229: in read        
    raise OSError(
E   OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
----------------------------- Captured stdout ----------------------------- 

Si vous voulez utiliser un fichier texte personnel pour le jeu,
Assurez-vous que le fichier contienne un mot par ligne séparé par un Entrée 
Entrez le nom du fichier .txt sinon pressez Entrée:
============================ warnings summary ============================= 
pendu_game.py:119
  C:\Users\El familia\OneDrive\mp3\pendu_game.py:119: DeprecationWarning: invalid escape sequence \o
    print(" ___ \n | | \n |\o/ \n |\n |\n---")

pendu_game.py:122
  C:\Users\El familia\OneDrive\mp3\pendu_game.py:122: DeprecationWarning: invalid escape sequence \o
    print(" ___ \n | | \n |\o/ \n | | \n |\n---")

pendu_game.py:125
  C:\Users\El familia\OneDrive\mp3\pendu_game.py:125: DeprecationWarning: invalid escape sequence \o
    print(" ___ \n | | \n |\o/ \n | | \n |/ \ \n---")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html     
========================= short test summary info ========================= 
ERROR test_assertion.py - OSError: pytest: reading from stdin while output is captured!  Consider...
!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!! 
====================== 3 warnings, 1 error in 0.40s ======================= 
PS C:\Users\El familia\OneDrive\mp3> 
PS C:\Users\El familia\OneDrive\mp3>
