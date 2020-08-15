#Dada un cantidad en pesos, obtener la equivalencia en dólares, asumiendo que la unidad
#cambiaría es un dato desconocido.
cant_pesos=int(input("Digite su cantidad en pesos: "))
unidad = int(input("Digite la unidad a cambiar:"))
conversion =  cant_pesos * unidad
print(f"el equivalente es de: ",conversion)