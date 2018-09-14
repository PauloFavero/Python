# dado1 será um número, operador será o símbolo da operação e dado2 será o segundo número
# verificar a partir do numero inserido se é um valor inteiro ou float
#função input sempre retorna str, por isso usamos o isdigit para verificar se é inteiro ou float




dado1 = input()
if dado1.isdigit() :
  dado1 = int(dado1)
  tipo_operando1 = "int"
else:
  dado1 = float(dado1)
  tipo_operando1 = "float"

operador = str(input())

dado2 = input()
if dado2.isdigit() :
  dado2 = int(dado2)
  tipo_operando2 = "int"
else:
  dado2 = float(dado2)
  tipo_operando2 = "float"

#verificar as operaçoes possiveis
flag_error = 0
resultado = 0

if operador == "+":
    resultado = dado1 + dado2

elif operador == "-":
    resultado = dado1 - dado2

elif operador == "*":
    resultado = dado1  * dado2

#necessitamos verificar se não será dividido por zero
elif operador == "/":
   if dado2 == 0:
       print("Erro.")
       flag_error =1
   else:
        resultado = dado1 / dado2

#necessitamos verificar se não será dividido por zero

elif operador == "//":
    if dado2 == 0:
        print("Erro.")
        flag_error = 1
    else:
       resultado = dado1 // dado2

#necessitamos verificar se não será dividido por zero

elif operador == "%":
    if dado2 == 0:
        print("Erro.")
        flag_error = 1
    else:
     resultado = dado1 % dado2

elif operador == "**":
    resultado = dado1 ** dado2

else:
    print("Erro.")

if flag_error == 0:
 if type(resultado) == int:
    print(resultado)
 else:
    print(format(resultado, ".2f"))