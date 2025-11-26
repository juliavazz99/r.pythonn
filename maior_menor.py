quantidade = int(input("Quantos números deseja informar? "))

numeros = []

for i in range(quantidade):
    n = float(input("Digite um número: "))
    numeros.append(n)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
