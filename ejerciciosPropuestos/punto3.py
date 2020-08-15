#La presión, el volumen y la temperatura de una masa de aire se relacionan por la
#formula:
#masa = (presión * volumen)/(0.37 * (temperatura + 460))
volumen=int(input("Digite el volumen: "))
presion=int(input("Digite la presion: "))
temperatura=int(input("Digite la temperatura: "))
masa = (presion * volumen)/(0.37*(temperatura+460))
print(f"la masa es de: {masa}")