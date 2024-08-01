N = int(input("Qual será a ordem da matriz? "))

matriz: [[int]] = [[0 for x in range(N)]for x in range(N)]

for i in range(0, N):
    for j in range(0, N):
        matriz[i][j] = int(input(f"Elemento [{i}][{j}]: "))

soma = 0
for i in range(0, N):
    for j in range(0, N):
        if j > i:
            soma = soma + matriz[i][j]

print(f"Soma dos elementos acima da diagonal principal: {soma}")