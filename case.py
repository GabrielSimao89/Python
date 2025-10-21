opc=0

while True:
    print("1- Para receber um bom dia!")
    print("2- Para receber uma boa tarde!")
    print("3- Para receber uma boa noite!")
    print("4-Sair!")

    opc=int(input("Escolhe uma opção!"))

    match opc: 
        case 1:
            print("Bom Dia!")
        case 2:
            print("Boa Tarde!")
        case 3:
            print("Boa Noite!")
        case 4:
            print("Xau Xau!")
            break

