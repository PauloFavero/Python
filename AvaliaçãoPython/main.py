
def tupla_float_int(x) :
    x = x[1:-1]       # remove parênteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])   # converte primeiro elemento para float
    i = int(x[1])     # converte segundo elemento para int
    return (f,i)      # retorna tupla


notas_ac = [float(x) for x in input().split()]
notas_lab = [tupla_float_int(x) for x in input().split()]
nota_provas = [float(x) for x in input().split()]

p1 = float(nota_provas[0])
p2 = float(nota_provas[1])
Mp = (2*p1+3*p2)/5
freq = int(input())

Mac = 0.0
for i in notas_ac:
    Mac +=i
Mac = Mac/len(notas_ac)


Mlab = 0.0
div = 0.0
for i in notas_lab:
   Mlab += i[0]*(i[1])
   div +=i[1]
Mlab /= div


MElem = 0.6 * Mp + 0.3 * Mlab + 0.1 * Mac
Mpre = min(MElem, Mp, Mlab)
if(Mpre<5 and Mpre>=2.5):
        exame = float(input())

print("Média das atividades conceituais:", format(Mac, ".1f"))
print("Média das tarefas de laboratório:", format(Mlab, ".1f"))
print("Média das provas:", format(Mp, ".1f"))
print("Média ponderada dos elementos:", format(MElem, ".1f"))
print("Média preliminar:", format(Mpre, ".1f"))
if(Mpre<5 and Mpre>=2.5):
    print("Nota no exame:", format(exame, ".1f"))

if(freq>=75):
    if(Mpre>=5):
        print("Aprovado(a) por nota e frequência.")
        print("Média final:", format(MElem, ".1f"))
    elif(Mpre<5 and Mpre>=2.5):
        Mfinal =  (Mpre+exame)/2
        if(Mfinal>=5):
            print("Aprovado(a) por nota e frequência.")
            print("Média final:", format(Mfinal, ".1f"))
        else:
            print("Reprovado(a) por nota.")
            print("Média final:", format(Mfinal, ".1f"))
    else:
        print("Reprovado(a) por nota.")
        print("Média final:", format(Mpre, ".1f"))
else:
    print("Reprovado(a) por frequência.")
    print("Média final:", format(Mpre, ".1f"))