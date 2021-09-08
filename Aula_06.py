#Aula_06: Conjuntos e subconjuntos em Python

#Subconjunto
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('a é subconjunto de b: {}' .format(conjunto_subset))


conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('b é um subconjunto de a: {}' .format(conjunto_superset))

#----------------------------------------------------------------------

#Converter uma lista pra conjunto
lista = ['cachorro', 'gato', 'gato', 'lobo', 'arara']
print(lista)
conjunto_animais = set(lista)  
print(conjunto_animais)
lista_animais = list(conjunto_animais)      #convertendo para lista retirando duplicidade
print(lista_animais)




#----------------------------------------------------------------------

# #Unir os dois conjuntos
# conjunto = {1, 2, 3, 4, 5}
# conjunto2 =  {5, 6, 7, 8}
# conjunto_uniao = conjunto.union(conjunto2)
# print(conjunto_uniao)

# #Intersecção entre os conjuntos
# conjunto_interse = conjunto.intersection(conjunto2)
# print('Intersecção: {}' .format(conjunto_interse))

# #Diferenças entre conjuntos
# conjunto_dif = conjunto.difference(conjunto2)
# print('Diferença: {}' .format(conjunto_dif))

# #Diferença simétrica
# conjunto_difSim = conjunto.symmetric_difference(conjunto2)
# print('Diferença simétrica: {}' .format(conjunto_difSim))






#----------------------------------------------------------------------

# conjunto = {1, 2, 3, 4}
# conjunto.add(5)         #adicionar elemento ao conjunto
# conjunto.discard(2)     #remover
# print(conjunto)

