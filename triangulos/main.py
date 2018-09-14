# -*- coding: utf-8 -*-
import sys

A = float(input())
B = float(input())
C = float(input())

if  (A and B and C) <= 0:
    print("Valores inválidos na entrada.")
    sys.exit()
elif (A>(B+C)) or (B>(A+C)) or (C>(A+B)) :
    print("Valores inválidos na entrada.")
    sys.exit()

if B>A and B>C:
    aux = A
    A = B
    B = aux
elif C>A and C>B:
    aux = A
    A = C
    C = aux

Soma = B**2 + C**2

if A==B and A==C:
    print("Triângulo equilátero.")
elif A==B or B==C:
    print("Triângulo isósceles.")
else:
    print("Triângulo escaleno.")

if A**2 == Soma:
    print("Triângulo retângulo.")
elif A**2 < Soma:
    print("Triângulo acutângulo.")
else:
    print("Triângulo obtusângulo.")
