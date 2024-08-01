M: int
N: int

M = int(input("Qual a quantidade de linhas da matriz? "))
N = int(input("Qual a quantidade de colunas da matriz? "))

matriz: [[float]] = [[0 for x in range(N)]for x in range(M)]

for i in range(0, M):
    for j in range(0, N):
        matriz[i][j] = (input(f"Elemento [{i}][{j}]: "))

for i in range(0, M):
    for j in range(0, N):
        if matriz[i][j] < 0:
            print(matriz[i][j])