# laberinto
Camino solución de un laberinto

El laberinto se construirá a través de una matriz donde el usuario ingresa las letras y valores siguientes: una E (Entrada), una S (Salida), 0's (espacios libres para moverse, mínimo 3 ceros) y 1's (muros y no podemos desplazarnos, mínimo 3 unos). El camino solución debe mostrarse por X's al sustituirse la 'E', 'S' y los 0's en el laberinto (matriz).

Como usuarios ingresaremos las letras o valores separados por una coma (cada uno), posteriormente damos un “Enter” para terminar dicha columna y comenzar la siguiente columna, repetimos los pasos con la finalidad de agregar las columnas que deseamos y para concluir la matriz dejamos una fila en blanco (sin ingresar valores) y presionamos "Enter". 

Ejemplo: E, 0, 1, 1 (Enter) 1, 0, 0, 1 (Enter) 1, 1, 0, S (Enter) (fila vacia + Enter)

El programa nos mostrará por pantalla el camino solución desde la entrada o inicio hasta la salida y el camino recorrido por las letras "X's" (el código está diseñado para ejecutarse en IDE's para python o internamente en el sistema operativo).
