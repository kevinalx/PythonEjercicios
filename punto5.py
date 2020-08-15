#Un maestro desea saber que porcentaje de hombres y que porcentaje de mujeres hay en
#un grupo de estudiantes.
num_muj=float(input("Ingrese el numero de mujeres: "))
num_hom=float(input("Ingrese el numero de hombres: "))

total=num_muj+num_hom
por_hom=num_hom*100/total
por_muj=num_muj*100/total

print(f"El total de hombres es de: {por_hom}")
print(f"El total de mujeres es de: {por_muj}")
