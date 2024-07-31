M = int(input("Quantas linhas a matriz terá? "))
N = int(input("Quantas colunas a matriz terá? "))

mat: [[int]] = [[0 for x in range(N)] for x in range (M)]

for i in range (0, M):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]"))

print()
print("MATRIZ DIGITADA: ")
for i in range(0, M):
    for j in range(0, N):
        print(f"{mat[i][j]} ", end = "")
    print()