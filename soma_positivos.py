soma = 0

while True:
    numero = float(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    if numero > 0:
        soma += numero

print("Soma dos números positivos:", soma)
