diagrama_entrada = []

while (1):
    l = input()
    if l.isdigit():
        n = int(l)
        break
    else:
        l = l.split()
        diagrama_entrada.append(l)

altura = len(diagrama_entrada)
largura = len( diagrama_entrada [0] )


#for i in range (altura):
#    for j in range (largura):
#        print (diagrama_entrada [i][j], end="")
#    print ()

palavras = []
for p in range (n):
    palavras.append(input())

#print(palavras)

diagrama_saida = [["." for x in range(largura)] for y in range(altura)]


def horizontalDireita(p, largura, i, j, diagrama_entrada):

    aux = 0
    contador = 0
    for aux in range(len (p)):
        if j + aux < largura:
            if diagrama_entrada[i][j + aux] == p[aux]:
                contador = contador + 1
    if contador == len (p):
        return True
    else:
        return False
def horizontalEsquerda(p, i, j, diagrama_entrada):

    aux = 0
    contador = 0
    for aux in range(len (p)):
        if j - aux >= 0:
            if diagrama_entrada[i][j - aux] == p[aux]:
                contador = contador + 1
    if contador == len (p):
        return True
    else:
        return False

def verticalBaixo(p, altura, i, j, diagrama_entrada):

    aux = 0
    contador = 0
    for aux in range(len (p)):
        if i + aux < altura:
            if diagrama_entrada[i+aux][j] == p[aux]:
                contador = contador + 1
    if contador == len (p):
        return True
    else:
        return False

def verticalCima(p, i, j, diagrama_entrada):

    aux = 0
    contador = 0
    for aux in range(len (p)):
        if i - aux >= 0:
            if diagrama_entrada[i-aux][j] == p[aux]:
                contador = contador + 1
    if contador == len (p):
        return True
    else:
        return False

def diagonalDireita(p,i, j, diagrama_entrada):

    aux = 0
    contador = 0
    for aux in range(len (p)):
        if ((j + aux < largura)  and (i + aux < altura )):
            if diagrama_entrada[i+aux][j+aux] == p[aux]:
                contador = contador + 1
    if contador == len (p):
        return True
    else:
        return False

def diagonalEsquerda(p,i, j, diagrama_entrada):

    aux = 0
    contador = 0
    for aux in range(len (p)):
        if ((j - aux >=0)  and (i - aux >= 0 )):
            if diagrama_entrada[i-aux][j-aux] == p[aux]:
                contador = contador + 1
    if contador == len (p):
        return True
    else:
        return False

def diagonalDireitaCima(p,largura,i, j, diagrama_entrada):

    aux = 0
    contador = 0
    for aux in range(len (p)):
        if ((j + aux < largura)  and (i - aux >= 0 )):
            if diagrama_entrada[i-aux][j+aux] == p[aux]:
                contador = contador + 1
    if contador == len (p):
        return True
    else:
        return False

def diagonalEsquerdaCima(p,altura,i, j, diagrama_entrada):

    aux = 0
    contador = 0
    for aux in range(len (p)):
        if ((j - aux >=0)  and (i + aux < altura )):
            if diagrama_entrada[i+aux][j-aux] == p[aux]:
                contador = contador + 1
    if contador == len (p):
        return True
    else:
        return False

for p in palavras:
    for i in range (altura):
        for j in range(largura):
            if diagrama_entrada [i][j] == p [0]:

                if horizontalDireita(p, largura, i, j, diagrama_entrada):
                    for x in range (len(p)):
                        diagrama_saida [i] [j+x] = p[x]

                if verticalBaixo(p, altura, i, j, diagrama_entrada):
                    for x in range (len(p)):
                        diagrama_saida [i+x] [j] = p[x]

                if horizontalEsquerda(p, i, j, diagrama_entrada):
                    for x in range (len(p)):
                        diagrama_saida [i] [j-x] = p[x]

                if verticalCima(p, i, j, diagrama_entrada):
                    for x in range (len(p)):
                        diagrama_saida [i-x] [j] = p[x]

                if diagonalDireita(p, i, j, diagrama_entrada):
                    for x in range (len(p)):
                        diagrama_saida [i+x] [j+x] = p[x]

                if diagonalEsquerda(p, i, j, diagrama_entrada):
                    for x in range (len(p)):
                        diagrama_saida [i-x] [j-x] = p[x]

                if diagonalDireitaCima(p, largura, i, j, diagrama_entrada):
                    for x in range (len(p)):
                        diagrama_saida [i-x] [j+x] = p[x]

                if diagonalEsquerdaCima(p, altura, i, j, diagrama_entrada):
                    for x in range (len(p)):
                        diagrama_saida [i+x] [j-x] = p[x]
for i in range (altura):
    for j in range(largura):
        if j == largura:
            print (diagrama_saida [i] [j] , end = "")
        else:
            print (diagrama_saida [i] [j] , end = " ")
    print ()

