valor1 = int(input('Digite um número inteiro: '))
valor2 = int(input('Digite outro número inteiro: '))
#Vamos comparar os dois números e determinar qual deles é o maior:
if valor1 > valor2:
    print(f'O primeiro número, {valor1}, é maior que o segundo número, {valor2}')
else: #valor1 é < ou == ao valor2
    if valor2 > valor1: #caso valor2 > valor1
        print(f'O segundo número, {valor2}, é maior que o primeiro número, {valor1}')
    else:  #caso em que os dois valores são iguais
        print('Os dois números inseridos são iguais!')
print("Fim de execução do programa.")
