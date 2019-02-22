from math import trunc

def algoritmo_a(start,end):
    front = [[heu(start), start]]
    expanded = []
    expanded_nodes=0
    cnt = 0
    while front:
        i = 0
        for j in range(1, len(front)):
            if front[i][0] > front[j][0]:
                i = j
        #path maneja las rutas en los nodos
        path = front[i]
        #front maneja la heuristica con path
        front = front[:i] + front[i+1:]
        endnode = path[-1]

        #end es la forma estandar de salida
        if endnode == end:
            break
        if endnode in expanded: continue
        for k in movimientos(endnode):
            if k in expanded: continue
            newpath = [path[0] + heu(k) - heu(endnode)] + path[1:] + [k] 
            front.append(newpath)
            #guarda los nodos recorridos
            expanded.append(endnode)
            #cont de los endnodes
            cnt+=1
        #cnt = cnt+1
        #print(cnt)
        expanded_nodes += 1
        #print(path)
        if(cnt>20000):
            print("no tiene solucion")
            return cnt

    print ("Cantidad de extension de nodos:", expanded_nodes)
    print ("it:", cnt)
    print ("RESULTADO:")
    pp.pprint(path)


def movimientos(mat): 
    output = []  

    m = eval(mat)   
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); #blank space (zero)
    #Si i es 0 esta hasta arriba
    if i > 0:                                   
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
      output.append(str(m))
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
    #esta al fondo 
    if i < 3:                                   
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
      output.append(str(m))
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
    #J = 0 a la derecha al tope
    if j > 0:                                                      
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
      output.append(str(m))
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
    #j=3 a la izquiera al tope
    if j < 3:                                   
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
      output.append(str(m))
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
    #matriz con el movimiento hecho
    return output


def heu(puzz):
    distance = 0
    m = eval(puzz)          
    for i in range(4):
        for j in range(4):
            #mide la distancia entre nodos o lugar utopico
            if m[i][j] == 0: continue
            distance += abs(i - trunc(((m[i][j]-1)/4))) + abs(j -  ((m[i][j]-1)%4));
    return distance

#convertir la cadena en una matriz
def convert(cadena):
    cont = 0
    lista = []
    sc = list(cadena)
    m = []
    for x in sc:
        cont = cont + 1
        x = int(x,16)
        lista.append(x)
        #print(x)
        if (cont==(len(sc))**(0.5)):
            m.append(lista)
            cont = 0
            lista = []
    #convertir de hexa a decimal
    #m = hexa(m)
    return m

#convertir el hexadecimal
def hexa(matrix):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = int(matrix[i][j],16)
            
import pprint
pp = pprint.PrettyPrinter(indent=4)

if __name__ == '__main__':
    T=0
    while T == 0:
        #ingresa la cadena de la terminal
        cadena = str(input("Ingrese la cadena de caracteres: "))
        #cambia el punto de espacio vacio por un 0
        cadena = cadena.replace('.','0')
        #convertir la cadena a una lista y de una convierte el hexadecimal
        matriz = convert(cadena)
        m = str(matriz)
        print(m)
        if len(m)==0:
            T = 0
            print("cadena mal ingresada")
        else:
            T=1
            #m = str([[1, 2, 6, 3],[4, 9, 5, 7], [8, 13, 11, 15],[12, 14, 0, 10]])
            end = str([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])
            algoritmo_a(m,end)
    
