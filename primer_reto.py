#La función "solucion_laberinto" toma como argumento la matriz "laberinto".
def solucion_laberinto(laberinto):
    # Función auxiliar "busqueda" para encontrar el camino.
    def busqueda(x, y):
        # Indica la posición actual en (x, y) como visitada dentro de la matriz "visitado".
        visitado[x][y] = True
        
        # Verificamos si la posición de x,y == 'S', esto indica que hemos llegado al final del laberinto.
        if laberinto[x][y] == 'S':
            return True
        
        # Las Direcciones posibles: arriba, abajo, izquierda, derecha (se sigue un patron para el recorrido).
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        #Utilizamos un for para recorrer todas las direcciones posibles almacenadas en el laberinto.
        for dx, dy in direcciones:
            #En cada iteracción del bucle sumamos los valores "dx" y "dy" a las coordenadas actuales "x" y "y" almacenadas en "nx" y "ny".
            nx, ny = x + dx, y + dy
            # Verificamos si la próxima posición es: "válida y no ha sido visitada".
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] != '1' and not visitado[nx][ny]:
                # Llamar recursivamente a la función busqueda.
                if busqueda(nx, ny):
                    # Marcar el camino con 'X'.
                    laberinto[nx][ny] = 'X'
                    return True
        
        # No se encontró ninguna solución desde esta posición.
        return False
    
    # Obtenemos el número de filas y columnas del laberinto.
    filas, columnas = len(laberinto), len(laberinto[0])
    
    # Creamos una matriz para marcar las celdas visitadas. Estas se inicializan con "False", esto indicar que ninguna celda se ha visitado.
    visitado = [[False] * columnas for _ in range(filas)]
    
    # Encontramos la posición de inicio del laberinto (entrada).
    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] == 'E':
                laberinto[i][j] = 'X' 
                # Llamar a la función busqueda desde la posición de entrada
                busqueda(i, j) 
                # Rompemos el ciclo
                break
    
    #Devuelve el laberito modificado con las 'X'
    return laberinto

# Función para imprimir el laberinto con el formato deseado
def imprime_laberinto(laberinto):
    for columna in laberinto:
        # Imprimir cada fila con comas y comillas alrededor de los elementos
        print('[' + ', '.join(['"' + str(celda) + '"' for celda in columna]) + ']')

# Solicitar al usuario ingresar la matriz del laberinto
print("Ingrese el laberinto. Use 'S' para la salida, 'E' para la entrada, '0' para el camino y '1' para los obstáculos.")
print("Ingrese cada fila separada por comas y sin espacios.")
print("Cuando termine de ingresar todas las filas, presione Enter en una línea vacía.")

#Se crea una lista vacia llamada laberinto que almacena las filas del laberinto
laberinto = []
#Con el "while True" iniciamos un bucle infinito que permite al usuario ingresar filas del laberinto hasta que el usuario decida terminar la entrada ingresando una linea vacia
while True:
    fila = input().strip()
    if not fila:
        break
    # Separar la fila por comas y eliminar las comillas dobles
    fila = [celda.strip('"') for celda in fila.split(',')]
    laberinto.append(fila)

# La función "solucion_laberinto" procesa la matriz "laberinto" para guardar en la variable laberinto_resuelto
laberinto_resuelto = solucion_laberinto(laberinto)

# Imprimir el laberinto resuelto
print("Laberinto resuelto:")
imprime_laberinto(laberinto_resuelto)