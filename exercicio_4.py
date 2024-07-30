#Exercício 04
nome = input("Olá usuário, insira o seu nome: ")
idade = input("Quantos anos você tem, usuário? (somente número inteiro) ")
# print(len(nome)) -- Se o usuário não digita o nome, len(nome) = 0
if len(nome) != 0 and len(idade) != 0:
    print(f'O seu nome é {nome}')
    print("O seu nome invertido é ",nome[-1::-1]) #digamos que o nome seja Hugo: nome invertido é: nome[-1:-4:-1] ou nome[-1::-1]
    if ' ' in nome:
        print("O seu nome contém espaços")
        print("O seu nome possui ",(len(nome)-1),"letras")
    else:
        print("O seu nome não contém espaços")
        print("O seu nome possui ",(len(nome)),"letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[len(nome)-1]}") 
else:
    print("Desculpe, você deixou campos vazios.")
print("Obrigado por utilizar este programa.")
#Obs: esse programa funciona somente para nomes com 1 espaço!   
