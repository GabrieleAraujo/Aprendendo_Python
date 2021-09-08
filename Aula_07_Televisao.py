#Aula_07: Métodos, funções e classes
    #Função: retorna o valor
    #Método: Não retornar

#Televisão:
from typing import Mapping


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 6                          #definindo canal
    def power(self):
        if self.ligada:
            self.ligada = False

        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:                         #Quando TV ligada
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':    #Quando importar for o mesmo arquivo não imprime novamente

    #Estranciando a classe:
    televisao = Televisao()
    print('TV ligada: {}' .format(televisao.ligada))
    televisao.power()
    print('TV ligada: {}' .format(televisao.ligada))
    televisao.power()
    print('TV ligada: {}' .format(televisao.ligada))

    #aumentando canal com TV ligada
    print('Canal: {}' .format(televisao.canal))
    televisao.power()
    print('TV ligada: {}' .format(televisao.ligada))
    televisao.aumenta_canal()
    print('Canal +: {}' .format(televisao.canal))

    #Diminiuindo canal
    televisao.diminui_canal()
    print('Canal -: {}' .format(televisao.canal))

