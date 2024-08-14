# Função para encontrar o maior e o menor valor em um dicionário
def encontrar_maior_menor(dicionario):
    if not dicionario:
        return None, None  # Retorna None se o dicionário estiver vazio

    # Inicializa as variáveis para armazenar o maior e o menor valor
    maior_valor = float('-inf')  # Menor número possível
    menor_valor = float('inf')    # Maior número possível

    # Itera sobre os valores do dicionário
    for valor in dicionario.values():
        if valor > maior_valor:
            maior_valor = valor  # Atualiza o maior valor
        if valor < menor_valor:
            menor_valor = valor   # Atualiza o menor valor

    return maior_valor, menor_valor

# Exemplo de uso
dicionario_exemplo = {
    'a': 10,
    'b': 20,
    'c': 5,
    'd': 30,
    'e': 15
}

maior, menor = encontrar_maior_menor(dicionario_exemplo)
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')