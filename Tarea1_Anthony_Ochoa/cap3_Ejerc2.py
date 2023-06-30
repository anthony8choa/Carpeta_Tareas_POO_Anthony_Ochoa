try:
    horas = float(input("Introduzca las Horas: "))
    tarifa = float(input("Introduzca la Tarifa por hora: "))

    if horas <= 40:
        salario = horas * tarifa
    else:
        horasExtra = horas - 40
        salarioBase = 40 * tarifa
        salarioExtra = horasExtra * (tarifa * 1.5)
        salario = salarioBase + salarioExtra

    print("Salario:", salario)

except ValueError:
        print("Error, por favor introduzca un número")