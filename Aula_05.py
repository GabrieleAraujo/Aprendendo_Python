#Aula_05: Operações em lista/tupla

#TUPLA

lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
print(lista_animal[1]) 
print(sum(lista))       #soma todos os elementos da lista
print(max(lista))       #maior valor da lista
print(min(lista))       #menor valor



tupla = (1, 10, 12, 14)
print(tupla[1])
print(len(tupla))           #retorna a quantidade de elementos

#Converter lista para tupla
tupla_animal = tuple(lista_animal)
print(tupla_animal)

#Converter tupla em lista
lista_num =  list(tupla)
print(lista_num)
lista_num[0] = 100          #Alterar elemento na posição 0

#----------------------------------------------------------------------


# #LISTA
# lista = [12, 10, 7, 5]
# lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
# print(lista_animal[1]) 
# print(sum(lista))       #soma todos os elementos da lista
# print(max(lista))       #maior valor da lista
# print(min(lista))       #menor valor


#----------------------------------------------------------------------

# #Ordena a lista em ordem crescente
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)

# #Ordena em ordem decrescente 
# lista_animal.reverse()
# print(lista_animal)

# #Percorre as listas
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print (soma)


#----------------------------------------------------------------------

# #Verificar se há elemento na lista
# if 'lobo' in lista_animal:
#     print('Há um gato na lista')

# else:
#     print ('Não existe. Será incluido')
#     lista_animal.append('lobo')  #inclui novos registros a lista
#     print(lista_animal)

# #  #retira o último elemento da lista ou pela posição
# # lista_animal.pop()               
# # print(lista_animal)

# # #tirar elemento da lista pelo nome
# # lista_animal.remove('elefante')
# # print(lista_animal)

#----------------------------------------------------------------------
