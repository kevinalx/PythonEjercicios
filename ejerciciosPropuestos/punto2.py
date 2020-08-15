#Leer un numero y escribir el valor absoluto del mismo.
num = int(input('Digite un numero: '))

if num >= 0:
    absoluto = num
    print(f"El valor absoluto es:", absoluto)
else:
    absoluto = num * -1
    print(f"El valor absoluto es",absoluto)