def somar_numeros(intervalo_inferior, intervalo_superior):
    # Inicializar a variável soma
    soma = 0

    # Iterar sobre os números no intervalo especificado
    for numero in range(intervalo_inferior, intervalo_superior + 1):
        soma += numero  # Adicionar o número à soma

    return soma  # Retornar a soma total


def main():
    # Definir os limites do intervalo
    intervalo_inferior = 50
    intervalo_superior = 100

    # Chamar a função para somar os números no intervalo
    resultado = somar_numeros(intervalo_inferior, intervalo_superior)

    # Imprimir o resultado da soma
    print(f"A soma dos números entre {intervalo_inferior} e {intervalo_superior} é: {resultado}")


# Verificar se o programa está sendo executado diretamente
if __name__ == "__main__":
    main()