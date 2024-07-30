#Exercício 7:
#O usuário irá inserir o primeiro número, o segundo número e o operador aritimético (+, -, * ou /)
#Aí, usando while, o programa python irá calcular a operação matemática e imprimir a resposta.
#como fazer isso? Vamos tentar:
numeros_validos = False #Já vimos que esse recurso se chama FLAG: PARA SABERMOS SE, DE FATO, OS NÚMEROS INSERIDOS SÃO VÁLIDOS OU NÃO.
lista_operadores = '+-/*'
while True:
    num1 = input('Insira um número: ')
    num2 = input('Insira outro número: ')
    operador = input('Insira o operador (+,-,/,*): ')
    try:
        num1_float = float(num1)
        num2_float = float(num2) #Se algum desses números não for inteiro ou com casas decimais, o programa pula para o 'except'
        numeros_validos = True
    except:
        numeros_validos = False
    if numeros_validos == False: 
        print('Pelo menos um dos números digitados não são válidos.') 
        continue #assim, o python irá voltar para o inicio do while para que os números 1 e 2 e o operador sejam reinseridos.
    if operador not in lista_operadores: #o operador digitado não é +,-,/ ou *
        print('O operador inserido não é válido')
        continue #assim, o python irá voltar para o inicio do while para que os números 1 e 2 e o operador sejam reinseridos.
    if len(operador) > 1: #se o usuário digitar mais de um operador, também haverá problema.
        print('Digite apenas 1 operador')
        continue
    #E, agora sim, podemos fazer as contas:
    if operador == '+':
        soma = num1_float + num2_float
        print(f'A soma de {num1_float} e {num2_float} é {soma}')
    elif operador == '-':
        diferenca = num1_float - num2_float
        print(f'A difereça de {num1_float} e {num2_float} é {diferenca}')
    elif operador == '*':
        multiplicacao = num1_float * num2_float
        print(f'A multiplicação de {num1_float} e {num2_float} é {multiplicacao}')
    else:
        divisao = num1_float/num2_float
        print(f'A divisão de {num1_float} e {num2_float} é {divisao}')
    sair = input('Deseja sair da calculadora?R: ')
    sair = sair.lower() #transformo a string com letras maíusculas e/ou minúsculas em string somente com letras minúsculas
    sair = bool(sair.startswith('s')) #essa string começa com 's'? Se sim, sair = True e se não, sair = False.
    if sair == True:
        break #se o usuário deseja sair da calculadora, o while é interrompido.

