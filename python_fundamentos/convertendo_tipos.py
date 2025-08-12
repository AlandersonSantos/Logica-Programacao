#CONVERSÃO DE TIPOS:

#Em algum momento vamos precisar converter um tipo STRING(TEXTO), para um tipo INT/FLOAT, para fazer operação

#INTEIRO PARA FLOAT:

preco = 10

print(float(preco)) #Retorna 10.0

preco = 25

print(float(preco)) #Retorna 25.0



#FLOAT PARA INTEIRO:

preco = 11.80

print(int(preco)) #Retorna 11

preco = 0.99

print(int(preco)) #Retorna 0


#NÚMERO PARA STRING(TEXTO):

preco = 10.80
idade = 23

print(str(preco)) #Retorna 10.8

print(str(idade)) #Retorna 23


#STRING PARA NÚMERO:

preco = "10.80"
idade = "45"

print(float(preco)) #Retorna 10.80(float)

print(int(idade)) #Retorna 45(int)


#ERRO DE CONVERSÃO:

preco = "Python"

print(float(preco)) #Retorna um ERROR

#OBS: Não podemos transformar CARACTERES em NÚMEROS
