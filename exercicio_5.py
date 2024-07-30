#Questão 01:
#Faça um programa que peça para o usuário digitar um número inteiro;
#informe se este número é par ou impar;
#caso o usuário não digite um número inteiro, informe que não é um número inteiro
number = input("Digite um número inteiro: ") #é str
condicao = '.' in number #é a condição para o número ser inteiro. 3 é inteiro, enquanto 3.4 não é inteiro.
if condicao is False: #o número é inteiro? é:
    number_int = int(number)
    restopar = number_int % 2 
    if restopar == 0: #o resto da divisão do número inteiro par por 2 é igual a 0
        print('O número é par.')
    else: #o número é impar
        print("O número é impar.")
else: #o número não é inteiro
    print("O número não é inteiro.")
#outras soluções para a Questão 01 (a minha deu certo, logo é válida):
#Em vez de usar a condição 'condicao', usaremos outra condição: a condicao2:
number = input("Digite um número inteiro: ")
condicao2 = number.isdigit() #essa função vê se somente números foram digitados na string, ou seja, se O QUE FOI DIGITADO NA STR É INT.
if condicao2 == True:
    number_int = int(number)
    restopar = number_int % 2 
    if restopar == 0: #o resto da divisão do número inteiro par por 2 é igual a 0
        print('O número é par.')
    else: #o número é impar
        print("O número é impar.")
else: #o número não é inteiro
    print("O número não é inteiro.")
#E a solução 3: usando try e except:
number = input("Digite um número inteiro: ")
try:
    number_int = int(number) #se o número nao for inteiro, haverá erro nesta linha e aí o código pula para o 'except'.
    restopar = number_int % 2 
    if restopar == 0: #o resto da divisão do número inteiro par por 2 é igual a 0
        print('O número é par.')
    else: #o número é impar
        print("O número é impar.")
except:
    print("O número não é inteiro.")
#Questão 02:
#Faça um programa que pergunte a hora ao usuário e, baseando-se nesse horário descrito, exiba a saudação apropriada:
#ex: 0h a 11h é bom dia; 12h às 17h é boa tarde e 18h às 23h é boa noite.
hora = input('Insira a hora atual, em números inteiros (Ex: 1h, 3h, 13h, 23h):' )
hora_int=int(hora)
if hora_int >= 0 and hora_int <= 11:
    print('Bom dia!')
elif hora_int >=12 and hora_int <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')
#Solução aprimorada: vamos verificar se o que o usuário inseriu no programa é um número!
hora = input('Insira a hora atual, em números inteiros(Ex: 1h, 3h, 13h, 23h):' )
try:
    hora_int=int(hora) #se o número nao for inteiro, haverá erro nesta linha e aí o código pula para o 'except'.
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >=12 and hora_int <= 17:
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print('Os dados inseridos não são números inteiros.')
#Questão 03:
#Faça um programa que peça o primeiro nome do usuário. 
#Se o nome possuir 4 letras ou menos, escreva "seu nome é curto"
#Se possuir entre 5 e 6 letras, escreva "seu nome é normal"
#se possuir mais que 6 letras, escreva "seu nome é muito grande":
nome = input("Digite o seu nome: ")
#nome com 4 letras possui len(nome) = 4; se tiver x letras: len(nome) = x.
letras = len(nome)
if letras <= 4:
    print("Seu nome é pequeno")
elif letras >=5 and letras <=6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")
#Solução aprimorada: e se o usuário não digitou nada? vamos contabilizar este caso:
nome = input("Digite o seu nome: ")
letras = len(nome)
if nome: #if nome is true, ou seja, se o usuário digitou algo dentro da string.
    if letras <= 4:
        print("Seu nome é pequeno")
    elif letras >=5 and letras <=6:
        print("Seu nome é normal")
    else:
        print("Seu nome é grande")
else:
    print("O usuário não inseriu seu nome.")

#Finalizamos o exercício 5.
