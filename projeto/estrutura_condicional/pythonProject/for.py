x: int
soma: int

soma = 0
x = int(input("Digite o primeiro numero: "))
for i in range(0, 3):
    x = int(input("Digite um numero: "))
    soma = soma + x

print(f"Soma = {soma}")