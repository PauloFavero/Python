algoritimo = str(input())
valores = [int(x) for x in input().split()]
size = len(valores)


def printQuadro(size, valores):
    print((size + 2) * '.')
    altura = max(valores)
    for linha in range(altura, 0, -1):
        print('.', end='')
        for aux in range(size):
            if (valores[aux] >= linha):
                if aux < size:
                    print('|', end = '')
                else:
                    print('|', end = '')
                    print('.')
            else:
                print(' ', end = '')
        print('.')

    print((size + 2) * '.')


def bubbleIteration(size, valores):
    count = 0
    for aux in range(0, size - 1, 1):
        if (valores[aux] > valores[aux + 1]):
            count += 1
            valores[aux], valores[aux + 1] = valores[aux + 1], valores[aux]
    printQuadro(size, valores)
    return count

#falta ver quando termina de ordenar

def insertionSort(size, valores):
    count = 0
    for index in range(1, size):

        currentvalue = valores[index]
        position = index

        while position > 0 and valores[position - 1] > currentvalue:
            count+=1
            valores[position] = valores[position - 1]
            position = position - 1

        valores[position] = currentvalue
        printQuadro(size, valores)
        return count


def selectionSort(size,valores):
   for fillslot in range(size-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if valores[location]>valores[positionOfMax]:
               positionOfMax = location

       temp = valores[fillslot]
       valores[fillslot] = valores[positionOfMax]
       printQuadro(size, valores)
       valores[positionOfMax] = temp
       printQuadro(size, valores)


if algoritimo == "bubble":
    count = bubbleIteration(len(valores), valores)
    while (count != 1):
        count = bubbleIteration(len(valores), valores)

elif algoritimo == "insertion":
    count = insertionSort(size, valores)
    while (count != 0):
        count = insertionSort(size, valores)

elif algoritimo == "selection":
    count = selectionSort(size, valores)
