# coding:utf-8 -- Permet des accents

#Operateurs
#**
# *, /, //, na ordem em que aparecerem na expressao.
# %
# + e -, na ordem em que aparecerem na expressao.

#rappel

#Booleans fonctions
#print(9 > 3)
#print((3*4)/2 != (2*3) )

#Operateurs conditionels
#if  CONDIÇÃO :
#             BLOCO DE CÓDIGO
#  elif  CONDIÇÃO :
#             BLOCO DE CÓDIGO
#  else :
#              BLOCO DE CÓDIGO

#Operateurs logiques
# and or, not

option = "oui"

while option == "oui":

    valeur = float(input("Entre le valeur d'action:"))
    comissionBase = 39 #valeur base

    if valeur <= 2500.00:
        if valeur*0.017+30 < comissionBase:
            valeur += comissionBase
        else:  valeur += valeur*0.017+30
    elif valeur >2500.00 and valeur <= 6250.00:
        valeur += valeur * 0.0066 + 56
    elif valeur > 6250.00 and valeur <= 20000.00:
        valeur += valeur * 0.0034 + 76
    elif valeur > 20000.00 and valeur <= 50000.00:
        valeur += valeur * 0.0022 + 100
    elif valeur > 50000.00 and valeur <= 500000.00:
        valeur += valeur * 0.0011 + 155
    elif valeur > 50000.00 and valeur <= 500000.00:
        valeur += valeur * 0.0011 + 155
    else: valeur += valeur * 0.009 + 255

    print(valeur)

    option = str(raw_input("voulez-vous faire un autre calcul ? oui ou no? "))

print("c'est fini")