
#funcao que cria uma copia de uma matriz
def copiaMatriz(m):
    n = len(m)
    copiaM = [[0]*n for i in range(0,n)]
    for i in range(1,n):
        copiaM[i] = m[i][:]
    return copiaM

#menu
def menu():
    m,b,n = entrada()
    print("Resolução pelo metodo de Gauss: ")
    imprimeLista(Gauss(copiaMatriz(m),b[:]))
    print("Resolução pelo metodo de Gauss com Pivoteamento")   
    imprimeLista(GaussPivoteamento(copiaMatriz(m),b[:]))
    print("Resolução pelo metodo de Decomposição LU: ")
    imprimeLista(decLU(copiaMatriz(m),b[:]))
    print("Resolução pelo metodo de Decomposição LU com Pivoteamento: ")
    imprimeLista(decLUPivoteamento(copiaMatriz(m),b[:]))
    return 0

#funcao que imprime uma matriz
def imprimeMatriz(matriz):
    size = len(matriz)
    for i in range(1,size):
        print("[",end = "")
        for j in range(1,size):
            if j+1 == size :
                print("{}".format(matriz[i][j]), end="")
            else:
                print("{} ".format(matriz[i][j]),end = "")
        print("]")


#funcao que imprime o vetor de resultados
def imprimeLista(lista):
    size = len(lista)
    for j in range(1,size):
        if j == size//2:
            print("x =  |{}|".format(lista[j]))
        else:
            print("     |{}| ".format(lista[j]))

#funcao que faz com que todos elementos da diagonal se tornem 1
def diagonal(m,b):
    n = len(m)
    for k in range(1,n):
        pivot = m[k][k]
        for i in range(1,n):
            m[k][i] = m[k][i]/pivot
        b[k] = b[k]/pivot
    return m,b

#le a entrada completa
def entrada():
    print("Digite a ordem da matriz: ")
    n = int(input())
    n = n+1
    matriz = [0]*n
    print("Digite os elementos da matriz: ")
    b = [0]*n
    for i in range(1,n):
        matriz[i] = [0]*n
        for j in range(1,n):
            print("A{}{}: ".format(i,j),end = "")
            matriz[i][j] = float(input())

    print("Digite os valores do vetor de resultados: ")
    for i in range(1,n):
        print("B{}: ".format(i),end = "")
        b[i] = float(input())
    return matriz,b,n

#funcao que resolve o sistema utilizando a decomposição LU com pivoteamento
def decLUPivoteamento(u,b):
    n = len(u)
    l = [0]*n
    p = [0] * n
    for i in range(1,n):
        l[i] = [0]*n
        p[i] = [0] * n
        p[i][i] = 1
    for k in range(1, n - 1):
        o = k
        for i in range(k + 1, n):
            if abs(u[i][k]) > abs(u[k][k]):
                o = i
        if o != k:
            aux = u[k][:]
            u[k] = u[o][:]
            u[o] = aux[:]
            pa = p[k][:]
            p[k] = p[o][:]
            p[o] = pa[:]
            la = l[k][:]
            l[k] = l[o][:]
            l[o] = la[:]
        l[k][k] = 1
        pivot = u[k][k]
        for i in range(k+1,n):
            x = (-1)*u[i][k]/pivot
            for j in range(1,n):
                u[i][j] = u[i][j] + x*u[k][j]
            l[i][k] = (-1)*x
        l[n-1][n-1] = 1
    pb = multiplica(p,b)
    y = substituicoes(l,pb,0)
    x = substituicoes(u,y,1)
    return x

#funcao que resolve o sistema utilizando a decomposição LU
def decLU(u,b):
    n = len(u)
    l = [[0]*n for i in range(0,n)]
    for k in range(1,n-1):
        pivot = u[k][k]
        l[k][k] = 1
        for i in range(k+1,n):
            x = (-1)*u[i][k]/pivot
            for j in range(1,n):
                u[i][j] = u[i][j] + x*u[k][j]
            l[i][k] = (-1)*x
    l[n-1][n-1] = 1
    y = substituicoes(l,b,0)
    x = substituicoes(u,y,1)
    return x

#funcao que transforma uma matriz em triangular inferior
def triangularlInferior(m,b,n):
    for k in range(n-1,1,-1):
        pivot = m[k][k]
        for i in range(k-1,0,-1):
            x = (-1)*m[i][k]/pivot
            for j in range(n-1,0,-1):
                m[i][j] = m[i][j] + x*m[k][j]
            b[i] = b[i] + x*b[k]
    return m,b

#funcao que transforma uma matriz em triangular superior
def triangularSuperior(m,b,n):
    for k in range(1,n-1):
        pivot = m[k][k]
        for i in range(k+1,n):
            x = (-1)*m[i][k]/pivot
            for j in range(1,n):
                m[i][j] = m[i][j] + x*m[k][j]
            b[i] = b[i] + x*b[k]
    return m,b

#funcao que transforma uma matriz em triangular superior com pivoteamento
def triangularSuperiorPivoteamento(m,b,n):
    p = [0]*n
    for i in range(1,n):
        p[i] = [0]*n
        p[i][i] = 1
    for k in range(1,n-1):
        o = k
        for i in range(k+1,n):
            if abs(m[i][k]) > abs(m[k][k]):
                o = i
        if o!=k:
            aux = m[k][:]
            m[k] = m[o][:]
            m[o] = aux[:]
            ba = b[k]
            b[k] = b[o]
            b[o] = ba
        pivot = m[k][k]
        for i in range(k+1,n):
            x = (-1)*m[i][k]/pivot
            for j in range(1,n):
                m[i][j] = m[i][j] + x*m[k][j]
            b[i] = b[i] + x*b[k]

    return m,b

#funcao que resolve o sistema utilizando o metodo de Gauss
def Gauss(m,b):
    n = len(m)
    m,b = triangularSuperior(m,b,n)
    r = substituicoes(m,b,1)
    return r

#funcao que resolve o sistema utilizando o metodo de Gauss Jordan
def GaussJordan(m, b):
    n = len(m)
    m,b = triangularSuperior(m,b,n)
    m,b = triangularlInferior(m,b,n)
    m,b = diagonal(m,b)
    return b

#funcao que resolve o sistema utilizando o metodo de gauss com pivoteamento
def GaussPivoteamento(m, b):
    n = len(m)
    m, b = triangularSuperiorPivoteamento(m, b, n)
    m, b = triangularlInferior(m, b, n)
    m, b = diagonal(m,b)
    return b

#funcao que multiplica uma matriz por um vetor
def multiplica(l,u):
    n = len(l)
    r = [0]*n
    for k in range(1,n):
        for j in range(1,n):
            r[k] += l[k][j]*u[j]
    return r

#funcao que resolve o sistema utilizando substituições retroativas e sucessivas
def substituicoes(matriz,b,t):
    n = len(matriz)
    x = [0]*n
    aux = 0
    if t == 0:
        x[1] = b[1] / matriz[1][1]
        for i in range(2,n):
            aux = 0
            for j in range(1,i):
                aux += matriz[i][j]*x[j]
            x[i] = (b[i] - aux)/matriz[i][i]
    else:
        x[n-1] = b[n-1] / matriz[n-1][n-1]
        for i in range(n-1,0,-1):
            for j in range(i+1,n):
                aux += matriz[i][j]*x[j]
            x[i] = (b[i] - aux)/matriz[i][i]
            aux = 0
    return x

menu()