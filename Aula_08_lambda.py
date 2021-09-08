
#Lambda: simplificando Aula_08_palavras

#Contador de palavras
from Aula_07_Calculadora import Calculadora


contador_letras = lambda lista: [len(x) for x in lista]  #retornando lista

lista_animais = ['gato', 'leao', 'tigre']
print('Contador de palavras: {}' .format(contador_letras(lista_animais)))

#---------------------------------------------------------------

#Calculadora 1
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

a = int(input('Insira o valor de a:'))
b = int(input('Insira o valor de b:'))

print('Soma: {}' .format(soma(a, b)))
print('Subtração: {}' .format(subtracao(a, b)))


#---------------------------------------------------------------

#Calculadora2 - Dicionário
print('\nCalculadora2 - Dicionário')
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicação': lambda a, b: a * b,
    'divisão': lambda a, b: a / b,
}

soma = calculadora['soma']
print('Soma: {}' .format(soma(10, 5)))