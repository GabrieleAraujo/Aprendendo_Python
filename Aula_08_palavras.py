
#Contador de palavras


def contador_letras(lista_palavras):
    contador = []                       #retornando lista
    
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)             #adicionando na lista

    return contador

if __name__ == '__main__':  


    lista = ['chachorro', 'gato']
    print(contador_letras(lista))