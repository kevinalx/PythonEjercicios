#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
#saber cuanto deberá pagar finalmente por su compra.

compra=float(input("Digite el valor de la compra: "))

desc=compra*0.15
pago_total=compra-desc

print(f"Su total a pagar es de: ${pago_total}")
