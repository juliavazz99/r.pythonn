qtd = int(input("Quantos alunos serão cadastrados? "))

nomes = []
notas = []

for i in range(qtd):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    nomes.append(nome)
    notas.append(nota)

print("\n--- Todos os alunos ---")
for i in range(qtd):
    print(nomes[i], "-", notas[i])

print("\n--- Alunos com nota >= 6 ---")
for i in range(qtd):
    if notas[i] >= 6:
        print(nomes[i], "-", notas[i])
