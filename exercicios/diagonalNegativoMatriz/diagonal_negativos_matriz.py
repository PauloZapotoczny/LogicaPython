N: int
negativos: int

N = int(input("Qual é a ordem da matriz? "))
matriz: [[float]] = [[0 for x in range(N)]for x in range(N)]

negativos = 0
for i in range(0, N):
    for j in range(0, N):
        matriz[i][j] = float(input(f"Elemento [{i},{j}]: "))
        if matriz[i][j] < 0:
            negativos = negativos + 1

print("Diagonal principal: ")
for i in range(0, N):
    for j in range(0, N):
        if i == j:
            print(f"{matriz[i][j]:.2f} ", end="")

print()
print(f"Quantidade de negativos: {negativos}")