segundos = int(input("Digite os segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundosrestantes = segundos % 60
print(horas, "horas,", minutos, "minuto(s) e", segundosrestantes, "segundo(s)")
 