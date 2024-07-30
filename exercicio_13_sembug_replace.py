#No exercício 13 original, eu não sabia que existia modos mais fáceis de manipular o cpf inserido.
# Posso transformar um cpf '746.824.890-70' em '74682489070' de um modo mais simples e com menos esforço mental. Como? Veja:
cpf_inserido = '746.824.890-70'
cpf_inserido_final = cpf_inserido.replace('.', '') #nessa primeira utilização do replace, substituí os pontos por caracter algum no cpf inserido.
cpf_inserido_final_2 = cpf_inserido_final.replace('-', '') #agora, removi o caracter '-'.
#replace: string = string.replace(<coisa que quero remover da variável>, <coisa que quero substituir no lugar da coisa a ser removida>)
print(cpf_inserido_final_2)
#Esse método vale somente para strings: '123', por exemplo, é uma string.

#Um problema que pode aparecer no exercício 13: como saber se o cpf não é '111.111.111-11' ou '222.222.222-22'? Veja que:
#Se os cpfs forem com somente números repetidos, como acima, o programa alegará que o cpf é válido, porém a realidade não é esta.
#Como ver se isso acontece com o cpf inserido?
cpf_inserido = '111.111.111-11'
cpf_inserido_final = cpf_inserido.replace('.', '') #nessa primeira utilização do replace, substituí os pontos por caracter algum no cpf inserido.

cpf_inserido_final_2 = cpf_inserido_final.replace('-', '') #agora, removi o caracter '-'.

cpf_repetido = cpf_inserido_final_2[0]*len(cpf_inserido_final_2)
if cpf_repetido == cpf_inserido_final_2:
    print('O CPF inserido não é válido')
else:
    print('O programa desenvolvido no exercício 13 continua sem problemas.')

