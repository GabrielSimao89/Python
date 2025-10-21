import random    

escolhas = ["pedra", "papel", "tesoura"]
jogador = input("Pedra, papel ou tesoura? ").lower()
computador = random.choice(escolhas)

print(f"Computador: {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você venceu!")
elif jogador not in escolhas:
    print("Escolha inválida!")
else:
    print("Computador venceu!")
    