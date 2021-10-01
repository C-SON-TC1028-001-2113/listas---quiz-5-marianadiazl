def matriz(lista) :
    diagonal = []
    for i in range(len(lista)) :
        diagonal.append(lista[i][i])
    return(diagonal)

def main():
    lista = []
    fila = int(input(''))
    columna = int(input(''))
    if fila == columna :
        for i in range(fila) :
            lista.append([])
            for j in range(columna) :
                n = int(input())
                lista[i].append(n)
        resultado = matriz(lista)
        print(resultado)
    else :
        print('La matriz no es cuadrada')
  

if __name__=='__main__':
    main()
