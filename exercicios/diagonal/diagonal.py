import math

x = float(input("Digite o valor da base do retangulo: "))
y = float(input("Digite o valor da altura do retangulo: "))

area = x * y
perimetro = (x * 2) + (y * 2)
diagonal = math.sqrt(x ** 2 + y ** 2)

print(f"AREA = {area}")
print(f"PERIMETRO = {perimetro}")
print(f"DIAGONAL = {diagonal:.4f}")