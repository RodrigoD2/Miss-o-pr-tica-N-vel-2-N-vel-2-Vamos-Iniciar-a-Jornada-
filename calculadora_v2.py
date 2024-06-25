saida = ""
def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Não foi possível realiazar a divisão por 0"
    else:
        return a / b

def calculadora(n1, n2, operacao):
    if operacao == "+" or operacao == "soma":
        return soma(n1, n2)
    elif operacao == "-" or operacao == "subtracao":
        return subtracao(n1, n2)
    elif operacao == "*" or operacao == "multiplicacao":
        return multiplicacao(n1, n2)
    elif operacao == "/" or operacao == "divisao":
        return divisao(n1, n2)
    else:
        return "Operação inválida!"

while saida.lower() != "n":
    n1 = float(input("Digite o primeiro número:"))
    operacao = input("Digite a operacão:")
    n2 = float(input("Digite o segundo número:"))
    resultado = calculadora(n1, n2, operacao)
    print("O resultado da operação é:", resultado)

    saida = input("Deseja continuar? (s/n): ")
    print("Fim do programa!")
