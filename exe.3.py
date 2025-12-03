numero = int(input("Digite um número inteiro: "))

match numero:
    case _ if numero < 0:
        print("negativo")
    
    case 0:
        print("zero")
    
    case _ if numero > 0:
        if numero % 3 == 0 and numero % 5 == 0:
            print("divisivel por 3 e 5")
        elif numero % 2 == 0:
            print("positivo e par")
        elif numero % 2 != 0:
            print("positivo e impar")
        else:
            print("outros numeros positivos")
