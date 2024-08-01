N = int(input("Qual a quantidade de linhas da matriz? "))
M = int(input("Qual a quantidade de colunas da matriz? "))

matriz: [[float]] = [[0 for x in range(M)]for x in range(N)]

for i in range(0, N):
    print(f"Digite os elementos da {i + 1}a. linha: ")
    for j in range(0, M):
        matriz[i][j] = float(input(f"Elemento [{i}][{j}]: "))

vetor: [[float]] = [0 for x in range(N)]

for i in range(0, N):
    soma = 0
    for j in range(0, M):
        soma = soma + matriz[i][j]
    vetor[i] = soma

print("VETOR GERADO: ")
for i in range(0, N):
    print(vetor[i])