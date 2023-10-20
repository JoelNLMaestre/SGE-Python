from asyncio.windows_events import NULL
from calendar import c
 # ejercicio 1 multiplicacion de matrices
def multiplicacionMatriz(a, b):
    
    sum = 0
    rowsA = len(a)
    columnsB = len(b[0])
    
    if(len(a[0]) == len(b)):
        
        c = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        
        for i in range(0,rowsA,1):
            for j in range(0,columnsB,1):
                for k in range(0,columnsB,1):
                    c[i][j] += a[i][k] * b[k][j]                
    return c
        

a=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
b=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
c = multiplicacionMatriz(a,b)
print(c)

# ejercicio 2 repeticiones

def repeticiones(matriz, vector):
    repes = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(0,len(matriz),1):
        for j in range(0,len(matriz[0]),1):
            repes[i][j] = repeticiones2(matriz[i][j],vector)
            
    print("Matriz generada sin ordenar")
    print(repes)
    for i in range(0,5,1):
        repes[i].sort()
        
    print("matriz ordenada")
    print(repes)
                
                       

def repeticiones2(i, vector):
    r = 0
    for k in range(0,len(vector),1):
        if(i == vector[k]):
            r += 1
    return r

matriz = [[2,2,3,2,1],[3,3,2,1,2],[5,6,1,2,1],[4,3,1,2,2],[1,2,2,2,3]]
vector = [3,4,3,2,1,4,2,3,2,1]

repeticiones(matriz,vector)


