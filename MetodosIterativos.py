def copiaMatriz(m):
    n = len(m)
    copiaM = [[0]*n for i in range(0,n)]
    for i in range(1,n):
        copiaM[i] = m[i][:]
    return copiaM

def imprimeMatriz(matriz):
    size = len(matriz);
    for i in range(1,size):
        print("[",end = "");
        for j in range(1,size):
            if j+1 == size :
                print("{}".format(matriz[i][j]), end="");
            else:
                print("{} ".format(matriz[i][j]),end = "");
        print("]");
    print()


#funcao que imprime o vetor de resultados
def imprimeLista(lista):
    size = len(lista);
    for j in range(1,size):
        if j == size//2:
            print("x =  |{}|".format(lista[j]));
        else:
            print("     |{}| ".format(lista[j]));
    print()


def CLinhas(matriz):
    n = len(matriz)
    for i in range(1,n):
        soma = 0
        for j in range(1,n):
            soma += matriz[i][j] if i!=j else 0
        if(abs(matriz[i][i]) < abs(soma)):
            return 0
    return 1
    
def CSassenfeld(matriz):
    n = len(matriz)
    beta = [0]*n
    for i in range(1,n):
        for j in range(1,n):
            beta[i] += matriz[i][j] if i!=j else 0 
        beta[i] /= matriz[i][i]   
    b = max(beta[i] for i in range(1,n))
    return 1 if b < 1 else 0

 
def entrada():
    print("Digite a ordem da matriz: ");
    n = int(input())
    n = n+1
    matriz = [[0]*n for i in range(0,n)]
    print("Digite os elementos da matriz: ")
    b = [0]*n
    x = [0]*n
    for i in range(1,n):
        for j in range(1,n):
            print("A{}{}: ".format(i,j),end = "");
            matriz[i][j] = float(input())
    print("Digite os valores do vetor de resultados: ")
    for i in range(1,n):
        print("B{}: ".format(i),end = "")
        b[i] = float(input())

    print("Digite o valor de epsilon:")
    epsilon = float(input())
    return matriz,b,n,epsilon


def jacobi(a,b,x,n,d,epsilon,k=0,limite = 20): 
    prox = [0]*n
    for i in range(1,n):
        for j in range(1,n):
            prox[i] += a[i][j]*x[j] if (i!=j) else 0
        prox[i] = (b[i] - prox[i])/a[i][i]
    newd = max(abs(x[i] - prox[i]) for i in range(1,n))
    if(newd>d):
        return 0,k
    if (d < epsilon or k+1 == limite):
        return prox,k
    else:
        return jacobi(a,b,prox,n,newd,epsilon,k+1)



def seidel(a,b,x1,n,d,epsilon,k=0,limite = 20): 
    x2 = x1[:]
    for i in range(1,n):
        soma = 0
        for j in range(1,n):
            soma += a[i][j]*x2[j] if (i!=j) else 0
        x2[i] = (b[i] - soma)/a[i][i]; 
    erro = max(abs(x1[i] - x2[i]) for i in range(1,n))
    if(erro>d):
        return 0,k
    if((d < epsilon or k+1 == limite)):
        return x2,k
    else:
        return seidel(a,b,x2,n,erro,epsilon,k+1)





def menu():
    a,b,n,epsilon = entrada()
    x  = [0]*n
    k = 0
    for i in range(1,n):
        x[i] = b[i]/a[i][i]

    if CLinhas(a) == 0:
        print("Não satisfaz o critério das linhas")

    x1,k = jacobi(a,b,x[:],n,10,epsilon)
    if(x1!=0):
        print("Solução pelo método de Gauss Jacobi:",end = "\n\n")
        imprimeLista(x1)
        print(k," Iterações",end = "\n\n")
    else:
        print("Não converge")
    print("########################################")
    if CSassenfeld(a) == 0:
        print("Não satisfaz o critério de Sassenfeld")

    x2,k = seidel(a,b,x[:],n,10,epsilon)
    if(x2==0):
        print("Não converge")
    else:
        print("Solução pelo método de Gauss Seidel:",end = "\n\n")
        imprimeLista(x2)
        print(k," Iterações",end = "\n\n")  


menu()
