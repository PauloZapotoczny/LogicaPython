idade: int
salario: float
genero: str
nome: str
altura: float

salario = 5800.5
idade = 20
altura = 1.86
genero = 'M'
nome = "Paulo"

print(f"O funcionario {nome}, ganha {salario:.2f} tem {idade} anos, com {altura} de altura e é do genero {genero}.")
print("O funcionario {:s}, ganha {:.2f} tem {:d} anos, com {:.2f} de altura e é do genero {:s}.".format(nome, salario, idade, altura, genero))