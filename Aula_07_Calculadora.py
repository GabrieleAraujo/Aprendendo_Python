#Aula_07: Métodos, funções e classes
    #Função: retorna o valor
    #Método: Não retornar


# MÉTODOS: definiçãoo

#Calculadora
class Calculadora:                              #criando uma classe
    def __init__(self, num1, num2):             #self referencia objeto
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):     
        return self.valor_a + self.valor_b               #retorno

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':  
    #Chamando soma de fora
    #Estanciando uma classe: chama automaticamente para a class
    a = int(input('Insira o valor de a:'))
    b = int(input('Insira o valor de b:'))
    calculadora = Calculadora (a, b)

    print('Valor de a: {}, Valor de b: {}'.format(calculadora.valor_a, calculadora.valor_b))
    print('Soma: {}' .format(calculadora.soma()))
    print('Subtração: {}' .format(calculadora.subtracao()))
    print('Multiplicação: {}'.format(calculadora.multiplicao()))
    print('Divisão: {}'.format(calculadora.divisao()))