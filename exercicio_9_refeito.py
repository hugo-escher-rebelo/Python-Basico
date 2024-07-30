#Exercício 09:
#Faça um jogo para o usuário adivinhar qual é a palavra secreta:
# eu, programador, irei propor uma palavra secreta e vou dar a possibilidade para que o usuário digite apenas uma letra - (ok);
#A letra que o usuário digitar vai ser conferida para ver se ela está dentro da palavra secreta - (ok);
#se a letra estiver dentro da palavra secreta, exiba a letra digitada - ;
#se não estiver, exiba '*' - ;
#Faça a contagem de tentativas do usuário - (ok);
#Faça a validação de dados: o usuário tem que digitar apenas 1 letra, e não várias! - (ok).
tentativas = 0
palavra_secreta = 'python'
tamanho_palavra_secreta = len(palavra_secreta)
letras_acertadas = '' #é o conjunto das letras acertas, só que não necessariamente está na ordem correta da palavra secreta.
while True:
    letra_inserida = input('Digite uma letra, para verificar na palavra secreta: ')
    #Realizando a validação de dados da letra inserida pelo usuário:
    if len(letra_inserida) != 1:
        print('Digite apenas uma letra.')
        continue #e o python retorna à linha 13. A validação de dados terminou aqui.
    tentativas += 1 #A tentativa começa a ser computada quando uma letra apenas é inserida.
    if letra_inserida in palavra_secreta:
        letras_acertadas += letra_inserida #o conjunto de letras acertadas cresce, porém fora de ordem da palavra secreta.
    palavra_formada = '' #A palavra formada deve ser igual À palavra secreta, ao final do programa.
    for letra_secreta in palavra_secreta: #vamos repetir todas as letras da palavra_secreta
        if letra_secreta in letras_acertadas: #quando o programa ver que uma letra desta palavra já tiver sido descoberta...
            palavra_formada += letra_secreta
        else: #Se a letra inserida não for nenhuma letra da palavra secreta...
            palavra_formada += '*' #... o resto dos caracteres da palavra formada estarão preenchidos por '*'.
    print('No momento, a palavra formada é', palavra_formada)     
    if palavra_formada == palavra_secreta: #esse if precisa estar fora do 'for' e dentro do 'while' para funcionar.
        print('O jogo da palavra secreta foi finalizado porque você descobriu a palavra secreta, que é: ', palavra_secreta)
        break 
    sair = input('Deseja sair do jogo de adivinhação da palavra secreta? (sim ou não): ')
    sair = sair.lower()
    if sair.startswith('s') is True:
        break #Se o usuário digitar qualquer palavra que comece com 's', o while é interrompido.
print('O jogo da palavra secreta foi finalizado com sucesso.')
print('Você fez uma quantidade de tentativas igual a', tentativas, 'neste jogo')