x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))
z = int(input("Terceiro valor: "))

menor: int
menor = 0

if (x < y) and (x < z):
    menor = x
elif y < z:
    menor = y
else:
    menor = z

print(f"Menor valor: {menor}")