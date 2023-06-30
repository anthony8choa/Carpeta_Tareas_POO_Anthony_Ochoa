'''Escribe un programa que le pida al usuario una temper-
atura en grados Celsius, la convierta a grados Fahrenheit e imprima
por pantalla la temperatura convertida'''

temp = float(input("Ingrese la temperatura: "))

far = (temp *9/5)+32
print("La temperatura convertida es de: ", far,"°F")
