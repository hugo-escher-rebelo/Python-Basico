#Exercício 8: montar um programa onde devemos fazer esta tarefa aqui ó:
#Em uma frase, quero saber se:
#(1) Qual a letra apareceu mais vezes na frase inserida.
#informação relevante: como contar quantas vezes uma letra apareceu em uma frase?
#frase = 'oi'
#print(frase.count('o')) #esse .count só funciona para strings :)
#Obs:
#'a' é diferente de 'ã'.
#Exercício 8:
frase = 'O Python é uma linguagem de programação multiparadigma. O Python foi criado por Guido van Rossum.'
indice = 0 
tamanho = len(frase)
qtd_aparicoes_letra_mais_popular = 0 #inicialmente, não temos uma letra mais popular.
letra_mais_popular = '' #e a letra mais popular ainda não existe.
letras_desconsideradas = '. ' #não quero contabilizar o ponto '.' e nem o espaço ' '.
while indice < tamanho: 
    frase = frase.lower()
    letra = frase[indice] #vamos considerar que letras maiúsculas são iguais às minusculas.
    qtd_aparicoes = frase.count(letra) #. Quantas vezes a letra (variável) selecionada se repete?
    #E como vamos desconsiderar espaços e pontos da frase nesta contabilidade?
    if letra == ' ' or letra == '.':
        indice += 1 #antes de colocarmos o continue, temos que adicionar 1 ao índice.
        continue #aí o python volta a ler a primeira linha do while
    #não sendo uma das letras desconsideradas, o programa continua a rodar normalmente.
    if qtd_aparicoes > qtd_aparicoes_letra_mais_popular: #se a letra analisada aparecer mais vezes que a letra mais popular,
        letra_mais_popular = letra #ela se torna a mais popular.
        qtd_aparicoes_letra_mais_popular = qtd_aparicoes #e o número de suas aparições é registrado.
    indice += 1
print(f'A letra que apareceu mais vezes nesta frase foi: {letra_mais_popular} - número de aparições = {qtd_aparicoes_letra_mais_popular}.')

#uma obs:
frase = 'aaaooo'
indice = 0 
tamanho = len(frase)
qtd_aparicoes_letra_mais_popular = 0 #inicialmente, não temos uma letra mais popular.
letra_mais_popular = '' #e a letra mais popular ainda não existe.
letras_desconsideradas = '. ' #não quero contabilizar o ponto '.' e nem o espaço ' '.
while indice < tamanho: 
    frase = frase.lower()
    letra = frase[indice] #vamos considerar que letras maiúsculas são iguais às minusculas.
    qtd_aparicoes = frase.count(letra) #. Quantas vezes a letra (variável) selecionada se repete?
    #E como vamos desconsiderar espaços e pontos da frase nesta contabilidade?
    if letra == ' ' or letra == '.':
        indice += 1 #antes de colocarmos o continue, temos que adicionar 1 ao índice.
        continue #aí o python volta a ler a primeira linha do while
    #não sendo uma das letras desconsideradas, o programa continua a rodar normalmente.
    if qtd_aparicoes >= qtd_aparicoes_letra_mais_popular: #se a letra analisada aparecer mais vezes ou igual que a letra mais popular,
        letra_mais_popular = letra #ela se torna a mais popular.
        qtd_aparicoes_letra_mais_popular = qtd_aparicoes #e o número de suas aparições é registrado.
    indice += 1
print(f'A letra que apareceu mais vezes nesta frase foi: {letra_mais_popular} - número de aparições = {qtd_aparicoes_letra_mais_popular}.')