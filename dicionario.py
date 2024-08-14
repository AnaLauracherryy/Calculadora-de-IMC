def contar_caracteres(frase):
    dicionario_contagem = {}
    for caractere in frase:
        if caractere in dicionario_contagem:
            dicionario_contagem[caractere] += 1
        else:
            dicionario_contagem[caractere] = 1
    return dicionario_contagem



def main():
    frase = input("Digite uma frase: ")
    resultado = contar_caracteres(frase)
    print("Contagem de caracteres:")
    for caractere, contagem in resultado.items():
        print(f'"{caractere}": {contagem}')
if _name_ == "_main_":
    ()