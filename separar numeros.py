def separar_numeros(lista):
    # Criar duas listas vazias para armazenar os números positivos e negativos
    positivos = []
    negativos = []

    # Iterar sobre cada número na lista
    for numero in lista:
        # Verificar se o número é positivo (ou zero)
        if numero >= 0:
            # Se for positivo, adicionar à lista de positivos
            positivos.append(numero)
        else:
            # Se for negativo, adicionar à lista de negativos
            negativos.append(numero)

    # Retornar as duas listas separadas
    return positivos, negativos


def main():
    # Solicitar a entrada do usuário
    entrada = input("Digite uma lista de inteiros separados por espaço: ")

    # Converter a entrada em uma lista de inteiros
    lista_inteiros = list(map(int, entrada.split()))

    # Chamar a função para separar os números
    positivos, negativos = separar_numeros(lista_inteiros)

    # Exibir os resultados
    print("Números positivos:", positivos)
    print("Números negativos:", negativos)


# Verificar se o programa está sendo executado diretamente (não importado como módulo)
if _name_ == "_main_":
    main()