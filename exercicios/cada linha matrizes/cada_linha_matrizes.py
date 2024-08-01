n: int
n = int(input("Qual a ordem da matriz? "))
maior: float

matriz: [[float]] = [[0 for x in range(n)]for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        matriz[i][j] = float(input(f"Elemento [{i}][{j}]: "))

print("Maior elemento de cada linha: ")
for i in range(n):
    maior = 0
    for j in range(0, n):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    print(maior)