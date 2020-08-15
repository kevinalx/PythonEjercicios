#Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas
#invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con
#respecto a la cantidad total invertida.
persona1=int(input("Digite la cantidad que desea aportar: "))
persona2=int(input("Digite la cantidad que desea aportar:"))
persona3=int(input("Digite la cantidad que desea aportar:"))
cantidadTotal=int(input("Digite la cantidad total invertida:"))

persona1 = persona1 * 100/cantidadTotal
persona2 = persona2 * 100/cantidadTotal
persona3 = persona3 * 100/cantidadTotal

print(f"cantidad invtida por persona 1: ${persona1}")
print(f"cantidad invtida por persona 2: ${persona2}")
print(f"cantidad invtida por persona 3: ${persona3}")

