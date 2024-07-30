#Exercício 7:
#O usuário irá inserir o primeiro número, o segundo número e o operador aritimético (+, -, * ou /)
#Aí, usando while, o programa python irá calcular a operação matemática e imprimir a resposta.
#como fazer isso? Vamos tentar:
#Obs: coisas a fazer neste programa:
#(1): Devemos arranjar um jeito de podermos realizar operações matemáticas repetidamente, como se faz na calculadora de verdade - ok;
#(2): Devemos tratar os dados: só aceitaremos fazer contas com números com casas decimais - ok;
#(3): Devemos tratar os dados: só faremos a conta com um operador válido inserido (não vai dar certo se o operador for outro além dos que queremos ou se aceitarmos dois ou mais operadores juntos) - ok;
#(4): Por fim, devemos realizar a operação matemática desejada pelo usuário - ok.
operador_valido = '+-/*'
#Exercício 7 refeito:
while True is True:
    num1 = input("Insira o primeiro número: ")
    num2 = input("Insira o segundo número: ")
    operador = input("Digite o operador matemático desejado (+-/*): ")
    try: 
        num1_float = float(num1)
        num2_float = float(num2)  #Se os dois números forem convertidos com sucesso para float, o usuário terá digitado números validos na calculadora e podemos continuar o programa.
    except:
        print("Pelo menos um dos dois números não é int ou float: por favor, somente insira números inteiros (int) ou com casas decimais (float) nesta calculadora.")
        continue #Se os números não forem válidos, a inserção de números será reiniciada.
    if operador in operador_valido and len(operador) == 1: #o operador inserido foi inserido com sucesso. Agora, vamos realizar as contas:
        if operador == '+':
            soma = num1_float + num2_float
            print(f'A soma de {num1_float} com {num2_float} é {soma}.')
        elif operador == '-':
            diferenca = num1_float - num2_float
            print(f'A diferença entre {num1_float} e {num2_float} é {diferenca}.')
        elif operador == '*':
            multiplicar = num1_float * num2_float
            print(f'A Multiplicação de {num1_float} com {num2_float} é {multiplicar}.')
        else:
            dividir = num1_float / num2_float
            print(f'A Divisão entre {num1_float} e {num2_float} é {dividir}.')
    else: #Se o operador não for inserido com sucesso.
        if operador not in operador_valido:
            print("O operador matemático inserido não é reconhecido pela calculadora. Por favor, insira operadores de +, -, * ou / nesta calculadora.")
            continue 
        else: #Se len(operador) > 1:
            print("Mais de um operador foram digitados ao mesmo tempo. Por favor, digite apenas 1 operador reconhecido nesta calculadora por vez.")
            continue 
    condicao = input('Deseja sair da calculadora? Se sim, digite "Sair": ') #isso é uma string, ok?
    condicao = condicao.lower() #transformo a string com letras maíusculas e/ou minúsculas em string somente com letras minúsculas
    condicao = bool(condicao.startswith('s')) #essa string começa com 's'? Se sim, sair = True e se não, sair = False.
    if condicao == True:
        break #Se o usuário tiver digitado 'sair' na condicao, o programa será encerrado.
print("A calculadora foi encerrada com sucesso :)")
