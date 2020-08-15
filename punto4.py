#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha
#calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

cal1=float(input("Digite su primera calificacion: "))
cal2=float(input("Digite su segunda calificacion: "))
cal3=float(input("Digite su tercera calificacion: "))
examen_f=float(input("Digite la calificacion del examen: "))
trabajo_f=float(input("Digite la calificacion del trabajo: "))

prom=(cal2+cal2+cal3)/3
por_par=prom*0.55
por_exf=examen_f*0.30
por_trf=trabajo_f* 0.15
cal_f=por_par+por_exf+por_trf

print(f"Su calificacion final es de: {cal_f}")
