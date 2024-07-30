#IMC (kg/m²)= peso (kg) /(altura(m)^2)
nome = "Hugo Escher Rebelo"
altura = 1.80
peso = 95
imc = peso/(altura**2)
print("O ",nome,"tem ",altura,"metros de altura, pesa ",peso,"quilogramas e seu IMC é ",imc)

#uma observação: uso de elipses (os trÊs pontinhos: ...)
#se eu escrever:
#hugo =
#print(hugo)
#viu? deu erro pois eu não atribui valor algum à variável hugo
#mas se eu escrever assim, não dará erro:
hugo = ...
print(hugo)
#por que? pois esses três pontos é um PLACEHOLDER: você pode preencher a variável depois e, enquanto isso, o programa não te incomodará com isso.
