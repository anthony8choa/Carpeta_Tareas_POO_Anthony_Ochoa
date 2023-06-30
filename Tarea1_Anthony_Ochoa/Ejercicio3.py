'''Escribe un programa para pedirle al usuario el número de
horas y la tarifa por hora para calcular el salario bruto'''

horas = int(input("Introduzca las horas: ")) 
tarifa = float(input("Introduzca la tarifa: "))

salario = horas * tarifa
print("Su salario es: ", salario)