lista = []

while True:
    item = input("Digite um item (ou 'fim' para parar): ")
    if item.lower() == "fim":
        break
    lista.append(item)

print("Lista de compras:", lista)

