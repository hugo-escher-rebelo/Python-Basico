'''
Enunciado do exercício 11:
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar (exibir com o enumerate) valores da sua lista.
Não permita que o programa dê pau com erros de índices inexistentes na lista.

OBS: somente a título de curiosidade: pois eu ainda não testei este comando. Como limpar o que é exibido no terminal? Basta:
import os
os.system('cls') #cls no windows e clear nos demais sistemas operacionais.
'''
lista = []
import os 
while True:
    acao = input('Você deseja [i]nserir valores à lista, [a]pagar valores da lista ou [l]istá-la - exibí-la? R: ')
    acao = acao.lower() #transformando o que o usuário digitou em letra minúscula.
    if acao.startswith('i'): #Se o usuário quiser inserir um valor na lista, inicialmente vazia.
        os.system('cls')
        item = input('Insira um item na sua lista de compras: ')
        if len(item) < 1: #Se o usuário não digitou nada em 'item'.
            print('Você não digitou nenhum item para ser inserido na lista de compras.')
            continue 
        else: #se o usuário digitou um item a ser comprado em 'item'.
            lista.append(item)
    elif acao.startswith('a'): #se o usuário quiser apagar algum valor da lista de compras:
        os.system('cls')
        if len(lista) < 1: #se a lista estiver vazia.
            print('A lista está vazia e, portanto, não é possível remover itens dela.')
            continue 
        else: #se a lista não está vazia e há itens dentro desta lista.
            indice = input('Insira o índice do item da lista que você deseja apagar da lista de compras: ')
            indice_int=int(indice)
            if indice_int < len(lista): #se o indice inserido existe dentro da lista.
                lista.pop(indice_int) #o item será removido aqui.
            else: #se esse indice não existe na lista.
                print('O índice digitado não existe nesta lista e, portanto, não foi possível remover nenhum item da lista de compras.')
                continue
    elif acao.startswith('l'): #se o usuário quiser listar todos os valores da lista.
        os.system('cls')
        if len(lista) < 1: #se a lista estiver vazia.
            print('A lista está vazia e, portanto, não é possível a exibir.')
            continue
        else: #se a lista não está vazia e há itens dentro desta lista.
            lista_enumerada = enumerate(lista)
            for item in lista_enumerada:
                indice, nome = item 
                print(indice, nome)
    else: #caso o comando inserido pelo usuário não for apagar, inserir e nem listar.
        os.system('cls')
        print('A ação inserida não foi reconhecida pelo programa. Por favor, digite outra ação.')
        continue
    sair = input('Deseja sair do programa? [s]im ou [n]ão? R: ')
    sair = sair.lower()
    if sair.startswith('s'): #se o usuário desejar sair do programa, o programa será interrompido.
        break 
    else: #caso contrário, não.
        continue
os.system('cls')
print('\nO programa foi finalizado com sucesso. Obrigado por utilizá-lo')




