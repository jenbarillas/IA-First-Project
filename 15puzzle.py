def algoritmo_a(start,end):

    front = [[heu(start), start]]
    expanded = []
    expanded_nodes=0
    while front:
        i = 0
        for j in range(1, len(front)):
            if front[i][0] > front[j][0]:
                i = j
        path = front[i]
        front = front[:i] + front[i+1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in expanded: continue
        for k in movimientos(endnode):
            if k in expanded: continue
            newpath = [path[0] + heu(k) - heu(endnode)] + path[1:] + [k] 
            front.append(newpath)
            expanded.append(endnode)
        expanded_nodes += 1
        print(endnode)
    print ("Expanded nodes:", expanded_nodes)
    print ("Solution:")
    pp.pprint(path)


def movimientos(mat): 
    output = []  

    m = eval(mat)   
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); #blank space (zero)

    if i > 0:                                   
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
      output.append(str(m))
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
      
    if i < 3:                                   
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
      output.append(str(m))
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:                                                      
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
      output.append(str(m))
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < 3:                                   
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
      output.append(str(m))
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

    return output


def heu(puzz):
    distance = 0
    m = eval(puzz)          
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0: continue
            distance += abs(i - (m[i][j]/4)) + abs(j -  (m[i][j]%4));
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
            #end = str([[0, 1, 2, 3],[4, 5, 6, 7], [8, 9, 10, 11],[12, 13, 14, 15]])
            algoritmo_a(m,end)
    
