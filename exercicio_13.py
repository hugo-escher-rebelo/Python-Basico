"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
#Etapa 01: Exercício 12 - Cálculo do primeiro dígito do cpf.

#Fase 01: Montando a lista de números inteiros, derivada do cpf inserido:
cpf_inserido = input("Insira o seu cpf aqui (Com os pontos e traço): ") #inserindo o cpf do usuário.
string_util = cpf_inserido[0:11] #criei uma string somente com os 9 primeiros números do cpf e dois pontos simples.
#print(string_util) - linha de checagem da string util.
string_cpf_util = string_util.split('.') #separei os 9 primeiros números em 3 conjuntos de números (strings) com 3 algarismos. ex: lista = ['123', '456', '789']
#print(lista_cpf_util) - linha de checagem da lista_cpf_util 
string_cpf_util_final = ''.join(string_cpf_util) #precisamos unir essas 3 strings em uma única string.
#print(string_cpf_util_final) - linha de controle da string_cpf_util_final.
lista_cpf = list(string_cpf_util_final) #Transformando a string cpf_util_final em uma lista composta por strings de todos os algarismos do cpf
lista_cpf_int = []
for algarismo in lista_cpf:
    numero_int = int(algarismo)
    lista_cpf_int.append(numero_int)
#print(lista_cpf_int) #- esta linha era só para checar se a lista de números inteiros estava feita corretamente.
# Fase 02 - realizando as contas necessárias para gerar o primeiro dígito do cpf:
range_cpf = range(10, 1, -1)
indice = 0
soma = 0
for numero in range_cpf:
    soma += numero*lista_cpf_int[indice]
    indice += 1
#print(soma) - linha de checagem do valor da 'soma'.
soma = soma*10
resto = soma % 11 #resto adquirirá o resto da divisão entre soma e 11.
digito1 = 0 if resto > 9 else resto
print(f'\nO primeiro dígito do CPF inserido pelo usuário é igual a {digito1}')

#Etapa 02: Agora, vamos calcular o segundo dígito do cpf.

#Fase 01: Montando a lista de números inteiros + o primeiro dígito, derivada do cpf inserido pelo usuário:
string_cpf_util_final_2 = string_cpf_util_final + str(digito1) #somente estamos adicionando o digito 1 à 'string_cpf_util_final_2'
#print(string_cpf_util_final) - linha de controle da string_cpf_util_final.
lista_cpf_2 = list(string_cpf_util_final_2) #Transformando a string cpf_util_final_2 em uma lista composta por strings de todos os algarismos do cpf + o primeiro dígito calculado.
lista_cpf_int_2 = []
for algarismo in lista_cpf_2:
    numero_int = int(algarismo)
    lista_cpf_int_2.append(numero_int)
#print(lista_cpf_int_2) #- esta linha era só para checar se a lista de números inteiros estava feita corretamente.
# Fase 02 - realizando as contas necessárias para gerar o primeiro dígito do cpf:
range_cpf = range(11, 1, -1)
indice = 0
soma = 0
for numero in range_cpf:
    soma += numero*lista_cpf_int_2[indice]
    indice += 1
#print(soma) #- linha de checagem do valor da 'soma'.
soma = soma*10
resto = soma % 11 #resto adquirirá o resto da divisão entre soma e 11.
digito2 = 0 if resto > 9 else resto
print(f'\nO segundo dígito do CPF inserido pelo usuário é igual a {digito2}')
print('\nO Programa foi executado e finalizado com sucesso. \n')

#Etapa 03: Verificar se o cpf inserido pelo usuário é válido - é o exercício 14 (que eu farei somente porque insisti em inserir os cpfs com pontos e traços, ok?)
cpf_gerado = string_cpf_util_final_2 + str(digito2)
cpf_inserido = string_cpf_util_final + cpf_inserido[12:14]
if cpf_inserido == cpf_gerado:
    print('O CPF inserido é válido.\n')
else:
    print('O CPF inserido não é válido. \n')
print('O programa foi finalizado :) ')






