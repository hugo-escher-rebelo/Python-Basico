#Vamos fazer um exercício utilizando os recursos de while que aprendemos até agora:
#Enunciado: dada a seguinte variável:
#nome = 'Hugo Escher'
#Quero criar um novo nome:
#novo_nome = '*H*u*g*o* *E*s*c*h*e*r*'
#Lembre que cada letra da string tem um índice:
nome = 'Hugo Escher'
#indice:012345678910
#E o tamanho da string 'nome' é:
tamanho_nome = len(nome)
print(len(nome))

#Como farei isso? Vamos começar tentando criar uma string chamada nome = 'Hugo Escher' a partir de uma string vazia '':
novo_nome = ''
indice = 0
while indice < len(nome):
    nova_letra = nome[indice]
    novo_nome = novo_nome + nova_letra
    indice +=1
print(novo_nome)

#Ok...mas ainda falta adicionar os asteriscos '*' no novo_nome, ok? 
novo_nome = ''
indice = 0
while indice < len(nome):
    nova_letra = nome[indice] 
    novo_nome += f'*{nova_letra}' #no indice = 10, temos: novo_nome = '*H*u*g*o* *E*s*c*h*e*r'
    indice += 1
novo_nome += '*' #Agora sim, temos o novo_nome desejado pelo enunciado :)
print(novo_nome)

#Só para relembrar, pois senti muita dificuldade nisso: concatenação de strings:
string = 'a'
string2 = 'b'
string3 = string + string2
print(string3)
print(2*string)
print(3*string2)
print(4*string3)





    