N: int
N = int(input("Quantos numeros você irá digitar? "))

vet: [float] = [0 for x in range(N)]

for i in range (0, N):
    vet[i] = float(input("Digite um numero: "))

print()
print("Numeros digitados: ")
for i in range(0, N):
    print(f"{vet[i]:.1f}")
