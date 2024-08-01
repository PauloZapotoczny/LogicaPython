N: int
soma: float
media: float

N = int(input("Quantos números serão digitados? "))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um número: "))

soma = 0
print("VALORES = ", end="")
for i in range(0, N):
    print(f"{vet[i]:.2f} ", end="")
    soma = soma + vet[i]

media = soma / N
print()
print(f"SOMA = {soma}")
print(f"MEDIA = {media}")