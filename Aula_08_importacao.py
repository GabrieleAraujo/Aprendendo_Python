#Aula_08: Classes e métodos de módulo/lambda

#Módulos: arquivos .py

# import Aula_07_Televisao    #importando módulo 
# televisao = Aula_07_Televisao.Televisao()
# print(televisao.ligada)
# televisao.power()
# print(televisao.ligada)

#----------------------------------------------------------------


# #Importando a classe Televisao da Aula_07
# from Aula_07_Televisao import Televisao

# televisao = Televisao()
# print(televisao.ligada)
# televisao.power()
# print(televisao.ligada)

#----------------------------------------------------------------

# from Aula_07_Calculadora import Calculadora

# calculadora = Calculadora(5, 10)
# print(calculadora.soma())

#----------------------------------------------------------------

#Importando um método (função)
from Aula_08_palavras import contador_letras

lista = ['Gabi', 'Joe', 'Roberto']
print('Total de letras: {}' .format(contador_letras(lista)))