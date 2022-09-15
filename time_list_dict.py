#Créer une liste de longueur n

def fabrique_liste(n):
    L=[a for a in range(n)]
    return L

#Créer un dictionnaire de longueur n basé sur les valeurs de fabrique_liste(n)

def fabrique_dict(n):
    D={a**2:a for a in fabrique_liste(n)}
    return D

#Complexité temporelle

from time import time

def time_liste(n):
    L=fabrique_liste(n)
    time1=time()
    "a" in L
    time2=time()
    return time2-time1

def time_dict(n):
    D=fabrique_dict(n)
    time1=time()
    "a" in D
    time2=time()
    return time2-time1
