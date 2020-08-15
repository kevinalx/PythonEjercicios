cal_exa=float(input("Ingrese la calificacion del examen de matematicas: "))
cal_ta=float(input("Ingrese la calificacion del promedio de  tareas de matematicas: "))

cal_ex=float(input("Ingrese la calificacion del examen de fisica: "))
cal_tar=float(input("Ingrese la calificacion del promedio de tareas de fisica: "))

cal_exam=float(input("Ingrese la calificacion del examen de quimica: "))
cal_tare=float(input("Ingrese la calificacion del promedio de tareas quimica: "))

prom_mat1=cal_exa*0.90
prom_mat2=cal_ta*0.10

prom_fis1=cal_ex*0.80
prom_fis2=cal_tar*0.20

prom_qui1=cal_exam*0.85
prom_qui2=cal_tare*0.15

prom_mat=prom_mat1+prom_mat2/2
prom_fis=prom_fis1+prom_fis2/2
prom_qui=prom_qui1+prom_qui2/2
prom_total=prom_mat1*prom_mat2*prom_fis1*prom_fis2*prom_qui1*prom_qui2

print(f"El promedio de matematicas es de:{prom_mat}")
print(f"El promedio de fisica es de de: {prom_fis}")
print(f"El promedio de quimica es de: {prom_qui}")
print(f"El promedio total de las materias es: {prom_total}")