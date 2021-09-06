#Aula_02: Manipulação de variáveis

#Entrada de valores
a = int(input('Insira o valor de a:'))
b = int(input('Insira o valor de b:'))


soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a/b

print(type(soma)) #tipo de variável
#soma = str(soma) #convertendo interiro para string
#print('Convertido', type(soma))

print('Soma: '+ str(soma), subtracao, multiplicacao, int(divisao))

print('\nSoma: {}, \nSubtração: {}, \nMultiplicação: {}, \nDivisão: {}' .format(soma, subtracao, multiplicacao, divisao)) #Concatena o tipo
#\n quebra a linha

print('\nSoma: {soma}, \nSubtração: {subtracao},' 
      '\nMultiplicação: {multiplicacao},' 
      '\nDivisão: {divisao}'
       .format(soma=soma, subtracao=subtracao, 
        multiplicacao=multiplicacao, divisao=divisao)) #Concatena o tipo

