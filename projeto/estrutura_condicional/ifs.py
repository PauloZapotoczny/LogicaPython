x = int(input("Digite o horário do dia: "))

if x <= 12:
    print("Bom dia!")
elif (x > 12) and (x < 18):
    print("Boa tarde!")
else:
    print("Boa noite!")