# #Aula_03: Relação de variáveis

#Tirar média de notas
    #Inserindo notas:
a = int(input('Nota do primeiro bimestre:'))
if a > 10:
    a = int(input('Nota invalida. Insira novamente: '))

b = int(input('Nota do segundo bimestre:'))
if b > 10:
    b = int(input('Nota invalida. Insira novamente: '))

c = int(input('Nota do terceiro bimestre:'))
if c > 10:
    c = int(input('Nota invalida. Insira novamente: '))

d = int(input('Nota do quarto bimestre:'))
if d > 10:
    d = int(input('Nota invalida. Insira novamente: '))

#Cálculo da média
media = (a + b + c + d)/4

# #Limite de notas até 10
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('A média é: {}' .format(media))
# else:
#     print ('Erro: Foi inserido notas incorretas')


#Aprovado ou Reprovado
if media < 6:
    print('Você foi reprovado com: {}' .format(media))

else: 
    print('Você foi aprovado com: {}' .format(media))






# #Verificar se o número é Par ou Impar:
# a = int(input('Insira o valor de a:'))
# b = int(input('Insira o valor de b:'))

# resto_a = a % 2
# resto_b = b % 2

# if resto_a == 0 or resto_b == 0: not resto_b > 0: #not inverte a condicao
#     print('Foi inserido um número é par')
# else:
#     print('Todos impar')






# Entrada de valores e Condições IF, ELIF e ELSE
# a = int(input('Insira o valor de a:'))
# b = int(input('Insira o valor de b:'))
# c = int(input('Insira o valor de c:'))

# #Condições IF, ELIF e ELSE
# if a > b and a > c:
#     print('O maior número é  {}' .format(a))

# elif b > a and b > c:
#     print('O maior número é  {}' .format(b))

# else:
#     print('O maior número é  {}' .format(c))
