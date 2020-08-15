#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el
#vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
#ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
#base y comisiones.

sal_b=float(input("Digite su salario: "))
vta1=float(input("Ingrese el valor de la venta1: "))
vta2=float(input("Ingrese el valor de la venta2: "))
vta3=float(input("Ingrese el valor de la venta3: "))

total_vtas=vta1+vta2+vta3
com=total_vtas*0.10
total_pagar=sal_b+com

print(f"Su salario total es de: ${total_pagar}")
print(f"Sus comisiones son de: ${com}")