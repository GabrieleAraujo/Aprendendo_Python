#Aula_04: Laços de repetição 

#REPETIÇÃO COM FOR

# for x in range (1,100):               #repetição; range 1-99 
#     print(x)


#-------------------------------------------------------------------

# #Números primos
a = int(input('Entre com o número:'))
div = 0

#Percorrendo todos os números até a entrada 
for x in range (1,a+1):
    resto = a % x        #dividindo e pegando o resto pra ver se é divisivel com os números do laço
    print('N°: {}, Resultado: {}' .format(x, resto))
    if resto == 0:       
        div += 1         #div recebe 1 + ele mesmo

if div == 2:
    print('Número {} é primo' .format(a))
else:
    print('Número {} não é primo'.format(a))

#----------------------------------------------------------------------

#Imprimir números primos até o número inserido em a
# a = int(input('Entre com o número:'))

# for num in range (a+1):    #for num in range (100)
#     div = 0

#     for x in range(1, num + 1):
#         resto = num % x        #dividindo e pegando o resto pra ver se é divisivel com os números do laço
#         #print('N°: {}, Resultado: {}' .format(x, resto))
#         if resto == 0:       
#             div += 1         #div recebe 1 + ele mesmo

#     if div == 2:
#         print(num)

#----------------------------------------------------------------------

#REPETIÇÃO COM WHILE

# nota = int(input('Insira a nota: '))
# while nota > 10:
#     nota = int(input('Insira novamente a nota: '))


#Repetição de 0 - 10
# a = 0
# while a <= 10: 
#     print(a)
#     a +=1
