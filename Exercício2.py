#Gabriel Simão        15/10/2025               PI0924


print("Escolhe 3 números:")

num1 = int(input("Primeiro: "))
num2 = int(input("Segundo: "))
num3 = int(input("Terceiro: "))

# Encontrar o MAIOR usando ifs
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

# Encontrar o MENOR usando ifs
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print("maior", maior, "menor", menor)