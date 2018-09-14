# -*- coding: utf-8 -*-

# Lists are the most versatile of Python's
# compound data types. A list contains items separated by
# commas and enclosed within square brackets ([]). To some
# extent, lists are similar to arrays in C.
# One difference between them is that all the items
# belonging to a list can be of different data type.

# A tuple is another sequence data type that is similar to the list.
# A tuple consists of a number of values separated by commas.
# Unlike lists, however, tuples are enclosed within parentheses.
#
# The main differences between lists and tuples are:
# Lists are enclosed in brackets ( [ ] ) and their elements and
# size can be changed, while tuples are enclosed in parentheses ( ( ) )
# and cannot be updated. Tuples can be thought of as read-only lists.

# TR: Triângulo Retângulo
# TRI: Triângulo Retângulo Invertido
# TI: Triângulo Isósceles
# TII: Triângulo Isósceles Invertido
# A: Ampulheta
# E: Estrela

import  sys

ttuple_objetos = ('TR','TRI','TI','TII','A','E')
bValide_entry = True

def TR(ibase,scaracter):
    #range(inicio, fim, passo)
    for i in range(1, ibase+1, 2):
        print(i * scaracter)

def TRI(ibase,scaracter):
    #range(inicio, fim, passo)
    for i in range(ibase, 0, -2):
        print(i * scaracter)

def TI(ibase,scaracter):
    #range(inicio, fim, passo)
    for i in range(1, ibase+2, 2):
        print(int((ibase - i) / 2) * " ", end='')
        print(i * scaracter)
def TII(ibase,scaracter):
    #range(inicio, fim, passo)
    for i in range(ibase, 0, -2):
        k = int((ibase - i) / 2)
        print(k * " ", end='')
        print(i * scaracter)

def A(ibase,scaracter):
    # range(inicio, fim, passo)
    for i in range(ibase, 0, -2):
        k = int((ibase - i) / 2)
        print(k * " ", end='')
        print(i * scaracter)
    for i in range(1, ibase + 1, 2):
        if i!=1:
            print(int((ibase - i) / 2) * " ", end='')
            print(i * scaracter)

def E(ibase,scaracter):
    ilimite_1parte = (ibase-1)/2
    ilimite_2parte = ibase
    ilimite_3parte = (3*ibase + 1)/2
    ilimite_4parte = 2*ibase
    isize_estrela = 2*ibase
    #Ponta Superior
    k1 = 1
    y = ibase-2
    for i in range(1, isize_estrela+1, 1):
        if i<=ilimite_1parte:
            print(ibase * " ", end='')
            print(int((ibase - k1) / 2) * " ", end='')
            print(k1 * scaracter)
            k1+=2
        elif i==(ilimite_1parte+1):
            k1=1
            print(3*ibase * scaracter)
        elif i <= ilimite_2parte:
            print(int((ibase-y)/2) * " ", end='')
            print(y * scaracter, end='')
            print(int((ibase - y)+ibase) * " ", end='')
            print(y * scaracter)
            y-=2
        elif i<ilimite_3parte:
            if k1 != 1:
                print(int((ibase - k1) / 2) * " ", end='')
                print(k1 * scaracter, end='')
                print((2*ibase-k1) * " ", end='')
                print(k1 * scaracter)
            k1 += 2
        elif i == (ilimite_3parte):
            k1 = 1
            y = ibase-2
            print(3 * ibase * scaracter)
        else:
            print(ibase * " ", end='')
            print(int((ibase - y) / 2) * " ", end='')
            print(y * scaracter)
            y -= 2

stipo_objeto = str(input())
ibase = int(input())
scaracter = str(input())

if (stipo_objeto in ttuple_objetos):
    if (ibase%2==0):
        bValide_entry = False
        print('Base inválida.')

else:
    bValide_entry = False
    print('Objeto inválido.')
if not(bValide_entry):
    sys.exit()

if stipo_objeto == 'TR':
    TR(ibase,scaracter)
elif stipo_objeto == 'TRI':
    TRI(ibase,scaracter)
elif stipo_objeto == 'TI':
    TI(ibase,scaracter)
elif stipo_objeto == 'TII':
    TII(ibase,scaracter)
elif stipo_objeto == 'A':
    A(ibase,scaracter)
elif stipo_objeto == 'E':
    E(ibase,scaracter)