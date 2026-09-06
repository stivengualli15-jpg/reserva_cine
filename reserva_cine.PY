#Crear una matriz de 3 filas por 4 columnas llamada asientos, con todos los valores inicializados en 0.
#Pedir al usuario la fila y la columna del asiento que desea reservar.
#Marcar ese asiento como reservado asignándole el valor 1.
#Mostrar la matriz completa en formato de tabla utilizando bucles anidados.
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))
asientos[fila][columna] = 1
print("\nEstado de la sala:")
for i in range(len(asientos)):         
    for j in range(len(asientos[i])):   
        print(asientos[i][j], end=" ")  
    print()                             