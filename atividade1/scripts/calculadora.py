print("===== CALCULADORA BÁSICA =====")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)

if b != 0:
    print("Divisão:", a / b)
else:
    print("Divisão: não é possível dividir por zero")

c = float(input("Digite um número para calcular a raiz quadrada: "))
if c >= 0:
    print("Raiz quadrada:", c ** 0.5)
else:    print("Raiz quadrada: não é possível calcular a raiz quadrada de um número negativo")
print("fim da calculadora")
