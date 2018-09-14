import sys
N = int(input())

dictionaire = {} #dicionaria com chaves para cada tipo de individuo
envolvidos = [] # Lista com todos os individuos para percorrer por ordem alfabetica
detetives = {} # dicionario com os detetives e contem os valores de quantos casos resolveu
assassinos = {} # assassinos e suas vitimas

if N< 1 or N>100:
    print("Valor inválido na entrada.")
    sys.exit()

for i in range(0, N, 1):
    assassino, vitima, detetive = input().split()

    if i == 0:
        dictionaire['assassino'] = [assassino]
        dictionaire['vitima'] = [vitima]
        dictionaire['detetive'] = [detetive]
        detetives[detetive] = 1
        assassinos[assassino] = [vitima]
    else:
        if not (assassino in dictionaire['assassino']):
            dictionaire['assassino'].append(assassino)
        if not (vitima in dictionaire['vitima']):
            dictionaire['vitima'].append(vitima)
        if not (detetive in dictionaire['detetive']):
            dictionaire['detetive'].append(detetive)
        if not detetive in detetives:
            detetives[detetive] = 1
        else:
            detetives[detetive] = detetives[detetive] + 1
        if not (assassino in assassinos):
            assassinos[assassino] = [vitima]
        else:
            assassinos[assassino].append(vitima)

    if not (assassino in envolvidos):
        envolvidos.append(assassino)
    if not (vitima in envolvidos):
        envolvidos.append(vitima)
    if not (detetive in envolvidos):
        envolvidos.append(detetive)

ino = 0
ass = 0
det = 0

print(60 * "-")
for i in sorted(envolvidos):
    if (not (i in (dictionaire['assassino'])) and not (i in (dictionaire['detetive']))):
        print(i + " (in memoriam): vítima inocente.")
        #print(60 * "-")
    elif i in dictionaire['detetive']:
        if not (i in (dictionaire['vitima'])):
            print(i + ": detetive.")
            print("  Resolveu " + str(detetives[i]) + " caso(s).")

        else:
            print(i + " (in memoriam): detetive.")
            print("  Resolveu " + str(detetives[i]) + " caso(s).")

        if i in dictionaire['assassino']:
            for j in assassinos[i]:
                if (j in (dictionaire['detetive'])):
                    det += 1
                elif not (j in (dictionaire['assassino'])):
                    ino += 1
                else :
                    ass += 1
            if det > 0:
                print("  Matou " + str(det) + " detetive(s).")
            if ass > 0:
                print("  Matou " + str(ass) + " assassino(s).")
            if ino > 0:
                print("  Matou " + str(ino) + " inocente(s).")

            ass = 0
            det = 0
            ino = 0

        #print(60 * "-")
        ass = 0
        ino = 0
    else:
        if i in dictionaire['vitima']:
            print(i + " (in memoriam): assassino(a).")
            for j in assassinos[i]:
                if (j in (dictionaire['detetive'])):
                    det += 1
                elif not (j in (dictionaire['assassino'])):
                    ino += 1
                else :
                    ass += 1
            if det > 0:
                print("  Matou " + str(det) + " detetive(s).")
            if ass > 0:
                print("  Matou " + str(ass) + " assassino(s).")
            if ino > 0:
                print("  Matou " + str(ino) + " inocente(s).")

            ass = 0
            det = 0
            ino = 0

        else:
            print(i + ": assassino(a).")
            for j in assassinos[i]:
                if (j in (dictionaire['detetive'])):
                    det += 1
                elif not (j in (dictionaire['assassino'])):
                    ino += 1
                else :
                    ass += 1
            if det > 0:
                print("  Matou " + str(det) + " detetive(s).")
            if ass > 0:
                print("  Matou " + str(ass) + " assassino(s).")
            if ino > 0:
                print("  Matou " + str(ino) + " inocente(s).")

            ass = 0
            det = 0
            ino = 0

    det = 0
    ass = 0
    ino = 0
    print(60 * "-")

