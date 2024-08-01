M = int(input("Quantas linhas vai ter cada matriz? "))
N = int(input("Quantas colunas vai ter cada matriz? "))

matriza: [[float]] = [[0 for x in range(N)]for x in range(M)]
matrizb: [[float]] = [[0 for x in range(N)]for x in range(M)]

print("Digite os valores da matriz A: ")
for i in range(0, M):
    for j in range(0, N):
        matriza[i][j] = float(input(f"Elemento [{i}][{j}]: "))

print("Digite os valores da matriz B: ")
for i in range(0, M):
    for j in range(0, N):
        matrizb[i][j] = float(input(f"Elemento [{i}][{j}]: "))

soma = 0
print("MATRIZ SOMA: ")
for i in range(0, M):
    for j in range(0, N):
        soma = matriza[i][j] + matrizb[i][j]
        print(f"{soma:.1f} ", end="")
    print()