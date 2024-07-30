'''
Dada uma lista qualquer, exiba cada valor da lista da seguinte maneira:
0 Maria
1 Helena
2 Luiz
lista = ['Maria', 'Helena', 'Luiz']
'''
#Exercício 10:
lista = ['Maria', 'Helena', 'Luiz']
for nome in lista:
    indice = 0 #não sei quantos indices existem na lista, logo, usarei o 'While'.
    while indice < len(lista):
        if lista[indice] != nome:
            indice = indice + 1
            continue 
        else:
            print(indice, nome)
        indice = indice + 1
print(lista) 

#OBS: a função len também funciona com lista. logo: len(lista) = 3.
lista = ['Maria', 'Helena', 'Luiz']
tamanho_lista = len(lista)
print(f'len(lista) = {tamanho_lista}')

#Um modo mais simples de realizar o que eu fiz - esse é o gabarito oficial do exercício:
lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista)) #len(lista) = 3.
for indice in indices:  #for indice in range(0,3,1): indice vai de 0 a 2
    print(indice, lista[indice])
