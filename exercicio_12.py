"""
Calculo do primeiro dígito do CPF digitado pelo usuário.
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
#Exercício que gerará o primeiro digito, depois do traço, de um CPF qualquer.
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
digito = 0 if resto > 9 else resto
print(f'O primeiro dígito do CPF inserido pelo usuário é igual a {digito}')
#Fim do programa.
