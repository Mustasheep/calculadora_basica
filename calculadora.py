import art
print(art.logo)

def sinal(n1, n2):
    """A função tem o objetivo que calcular dois números de acordo com a operação escolhida:
multiplicação * , divisão / , soma + , subtraçao -
:param n1: 1º num int
:param n2: 2º num int
:return: resultado da operação
"""
    if operador == "+":
        return n1 + n2
    if operador == "-":
        return n1 - n2
    if operador == "*":
        return n1 * n2
    if operador == "/":
        div = n1 / n2
        if n1 % n2 == 0:
            return round(div)
        else:
            return round(div,4)

infinito = True
while infinito:
    numero_1 = int(input("\nDigite o primeiro número: "))
    ligar = True
    while ligar:
        operador = input("""
Soma            +
Subtração       -
Multiplicação   *
Divisão         /
    
Digite o operador: """)
        numero_2 = int(input("\nDigite o segundo número: "))
        resultado = sinal(numero_1,numero_2)
        print(f"\n{numero_1} {operador} {numero_2} = {resultado}")
        numero_1 = resultado
        nova_operacao = input(f"\nContinuar operação com {numero_1} ? Digite 's' ou 'n'  ").lower()
        if nova_operacao == "n":
            inicio = input("\nNovo cálculo? Digite 's' ou 'n'  ")
            if inicio == 's':
                ligar = False
            else:
                ligar = False
                infinito = False
        elif nova_operacao == "s":
            ligar = True
