#Basado en el código de este enlace
#https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/a-search-in-python/

from heapq import heappop, heappush
import heapq #Python ya trae una librería que te deja usar pilas
class aStar:
    recorrido = []

    def caminomascorto(self, tabla: list[list[int]]) -> int:
        print("\tMatriz:")
        for linea in tabla:
            print (linea)
        
        tam = len(tabla) #rows de la tabla
        
        if tam==0 or tabla[0][0]==1: #si no hay tabla o si el primer objeto es un obstáculo, se cierra
            return -1

        target = (tam-1,tam-1) #arbitrariamente hago que el objetivo sea la última celda
        f0 = 2*tam-2
        dirF = {(0,0): f0}#crea un diccionario donde se guardan las f de cada nodo
        
        #Los nodos en la pila van así: (f,g,fila,columna)
        pila = [(f0,1,0,0)]

        while pila:
            #Primero se saca de la pila el nodo que estamos analizando
            f,g,i,j = heappop(pila) #Esto regresa la pila variable por variable
            self.recorrido.insert(0,(i,j))
            #print(f"analizando nodo {i},{j} = {tabla[i][j]}")

            if (i,j) == target:
                return g

            #si el valor de f para este nodo es menor que el que está en el diccionario
            #dejamos de analizar el nodo y nos saltamos al siguiente
            if dirF[(i,j)] < f:
                continue

            #nodos adyacentes
            hijos = [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]
            for row,col in hijos:
                #verificamos que el camino esté despejado y que esté dentro de la tabla
                #porque con los hijos generamos celdas fuera de los límites
                #si el camino está despejado seguimos con la sig iteración
                if not (0<=row<tam and 0<=col<tam and tabla[row][col] == 0):
                    continue

                heuristica = max(abs(row-target[0]),abs(col-target[1]))
                nuevoF = heuristica + g + 1
                if nuevoF < dirF.get((row,col),float('inf')): #infinito si no encuentra el header
                    dirF[(row,col)] = nuevoF
                    heappush(pila,(nuevoF,g+1,row,col))
        return -1

    def printRecorrido(self):
        print("\n\tRecorrido:")
        for nodo in list(reversed(self.recorrido)):
            if(nodo!=(0,0)):
                print(f"-> {nodo}",end=" ")
            else:
                print(f"{nodo}", end=" ")
        


matriz = ((0,1,0,1,0),(0,0,0,0,1),(0,1,1,0,0),(1,1,0,0,0),(0,1,1,0,0))
astar=aStar()
astar.caminomascorto(matriz)
astar.printRecorrido()
