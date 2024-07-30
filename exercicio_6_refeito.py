#Vamos fazer um exercício utilizando os recursos de while que aprendemos até agora:
#Enunciado: dada a seguinte variável:
#nome = 'Hugo Escher' - o usuário irá inserir o nome dele aqui.
#Quero criar um novo nome:
#novo_nome = '*H*u*g*o* *E*s*c*h*e*r*'
nome = input('Insira o seu nome aqui: ')
tamanho_nome = len(nome) 
indice = 0 #Ex: Nome = Hugo; indice do 'o': 3 = len(nome) - 1
novo_nome = '' #A string vazia representa a variável na qual o novo nome será criado. Como criar esse novo nome?
while indice < tamanho_nome: 
    letra = nome[indice]
    nova_letra = f'*{letra}'
    novo_nome = novo_nome + nova_letra #novo nome = '*H*u*g*o' - falta um '*' depois do o.
    indice += 1
novo_nome = novo_nome + '*' #Adicionando o último asterisco necessário.
print(f'\n\n O novo nome é {novo_nome}')
print('\n\nFim de execução do programa.')


