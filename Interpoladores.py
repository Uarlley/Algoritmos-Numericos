import matplotlib.pyplot as plt

class Polinomio:
    def __init__(poly,grau,coef):
        poly.grau = grau
        poly.coef = coef

    def __lt__(self,other):
        return(self.grau >= other.grau)

#funcao que calcula um ponto no polinomio
def calculaPonto(polinomio,ponto):
    n = len(polinomio)
    ans = 0
    for i in range(0,n):
        ans += polinomio[i].coef*(ponto**polinomio[i].grau)
    return ans

#funcao que copia um polinomio
def copiaLista(x):
    copia = []
    n = len(x)
    for i in range(0,n):
        coeficiente = x[i].coef
        grau = x[i].grau
        aux = Polinomio(grau,coeficiente)
        copia += [aux]
    return copia

#funcao que encontra um elemento em uma lista
def find(grau,lista):
    n = len(lista)
    for i in range(0,n):
        if(grau==lista[i].grau):
            return i
    return -1

#funcao que soma dois polinomios
def somaPolinomio(p1, p2):
    n1 = len(p1)
    n2 = len(p2)
    ans = p1[:]
    for i in range(0,n2):
        pos = find(p2[i].grau,ans)
        if(pos>=0):
            ans[pos].coef += p2[i].coef
        else:
            ans += [p2[i]]

    return ans

#funcao que multiplica dois polinomios
def multPolinomio(p1,p2):
    n1 = len(p1)
    n2 = len(p2)
    ans = []
    for i in range(0,n1):
        for j in range(0,n2):
            coeficiente = p1[i].coef*p2[j].coef
            grau = p1[i].grau + p2[j].grau
            x = Polinomio(grau,coeficiente)
            if(len(ans) == 0):
                ans += [x]
            else:
                ans = somaPolinomio(ans,[x])
    return ans

#funcao que lê um polinomio
def lePolinomio():
    print("Digite o grau do polinomio:",end = "")
    n = int(input()) + 1
    x = []
    for i in range(0,n):
         print("Digite o coeficiente do elemento de grau {}:".format(i),end = "")
         coeficiente = float(input())
         aux = Polinomio(i,coeficiente)
         x += [aux]

    return x


#funcao que imprime um polinomio
def imprimePoly(x):
    n = len(x)
    for i in range(0,n):

        if(i != 0 and x[i].coef > 0):
            print(" +", end = "")

        if (x[i].coef != 0):
            if(x[i].grau == 0):
                print(" {}".format(x[i].coef), end="")

            if(x[i].grau == 1):
                print(" {}x".format(x[i].coef), end="")

            if(x[i].grau > 1):
                print(" {}x^({}) ".format(x[i].coef, x[i].grau), end="")

    print()

#funcao que le os pontos de entrada
def entrada():
    #print("Digite a quantidade de pares de pontos:")
    pontos = int(input())
    x = [0.0]*(pontos)
    y = [0.0]*(pontos)
    #print("Digite os valores de x:")
    for i in range(0,pontos):
        #print("x{}:".format(i),end = "")
        x[i] = float(input())

    #print("Digite os valores de f(x):")
    for i in range(0,pontos):
        #print("f(x{}):".format(i),end = "")
        y[i] = float(input())

    return x,y

#funcao que cria um polinomio de grau 1, definido por (x - ponto)
def criaPoly(ponto):
    ans = []
    ans+= [Polinomio(1,1)]
    if(ponto!=0):
        ans += [Polinomio(0, (-1)*ponto)]

    return ans

#funco que multiplica o polinomio por uma constante
def  multPorConstante(constante,lista):
    n = len(lista)
    for i in range(0,n):
        lista[i].coef *= constante
    return lista

#funcao que utiliza o método de lagrange
def lagrange(x,y):
    n = len(x)
    print(n)
    P = []
    L = [[] for i in range(0,n)]
    for k in range(0,n):
        aux = [Polinomio(0, 1)]
        for j in range(0,n):
            if(j!=k):
                polinomio = criaPoly(x[j])
                aux = multPolinomio(polinomio,copiaLista(aux))
                aux = multPorConstante(1/(x[k] - x[j]),copiaLista(aux))

        aux = multPorConstante(y[k],copiaLista(aux))
        L[k] = copiaLista(aux)
        P  = somaPolinomio(copiaLista(P),copiaLista(aux))
    return P

#funcao que utiliza o método de newton
def newton(x,y):
    n = len(x)
    p = [Polinomio(0,y[0])]
    for i in range(1,n):
        aux = [Polinomio(0,1)]
        for j in range(0,i):
            aux = multPolinomio(aux,criaPoly(x[j]))
        d = f(0,i,x,y)
        aux = multPorConstante(d,aux)
        p = somaPolinomio(p,aux)
    return p

#funcao que calcula um operador de diferênças divididas
def f(pos1,pos2,x,y):
    if(pos1+1==pos2):
        return (y[pos2] - y[pos1])/(x[pos2]-x[pos1])
    else:
        return (f(pos1+1,pos2,x,y) - f(pos1,pos2-1,x,y))/(x[pos2]-x[pos1])


#funcao que calcula a matriz de diferênças divididas
def matrizD(x,y):
    n = len(x)
    matriz = [[0]*n for i in range(0,n)]
    matriz[0] = y[:]
    for i in range(1,n):
        for j in range(0,n-i):
            matriz[i][j] =  (matriz[i-1][j+1] - matriz[i-1][j])/(x[i+j]-x[j])
    return matriz

#funcao que calcula o erro
def erro(x,matriz,ponto):
    E = 1
    n = len(x)
    if(n==len(matriz[0])):
        return 0
    for i in range(0,n):
        E *= (ponto - x[i])
    E = abs(E)
    E *= abs(max(matriz[n],key = abs))
    return E

#funcao que mostra o grafico do polinomio resultante
def grafico(polinomio,x,y):

    fig, ax = plt.subplots(figsize=(10, 5))

    #plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

    text = "$"
    n = len(polinomio)
    for i in range(0,n):
        if(polinomio[i].coef != 0):
            if(i != 0 and polinomio[i].coef > 0):
                text += "+"
            text += str(round(polinomio[i].coef,2))
            if(polinomio[i].grau) > 1:
                text += "x^{" + str(polinomio[i].grau) + "}"
            if(polinomio[i].grau) == 1:
                text += "x"
    text += "$"

    plt.plot(x, y, label= text, color='#1F77B4', marker='o', lw=2, markersize=8,
             markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')

    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=1.0)
    ax.xaxis.grid(True,linestyle='-', which='major', color='lightgrey', alpha=1.0)


    fontSize = 12
    ax.set_axisbelow(True)

    plt.xlabel(r'x', fontsize=fontSize + 2)
    #ax.xaxis.set_label_coords(0.5, -0.1)
    plt.ylabel(r'P(x)', fontsize=fontSize + 2)
    plt.yticks(fontsize=fontSize)
    leg = plt.legend(fontsize=fontSize)

    leg.set_title('', prop={'size': fontSize + 2})

    plt.show()
    plt.tight_layout()
    #plt.savefig('polinomio', bbox_inches='tight')
    plt.close()

def main():

    #definção dos pontos
    x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    y = [507712, 50220, 1896, 4, 0, 12, 2200, 54756, 540864]

    while(True):
        n1 = len(x)
        while(True):
            print("Digite o grau do polinômio interpolador: ", end="")
            n2 = int(input())
            if(n2 < n1):
                break
            else:
                print("Grau inválido! Tente novamente")
        n2 = n2+1
        print("Escolha o método a ser utilizado: \n1 : Lagrange\n2 : Newton")
        metodo = int(input())
        print("\nPontos disponíveis: ")
        for i in range(0,n1):
            print("{} : ({},{})".format(i+1,x[i],y[i]))

        newX = [0.0]*n2
        newY = [0.0]*n2
        print("Digite quais dos pontos deseja utilizar: ")
        for i in range(0,n2):
            pos = int(input())
            newX[i] = x[pos-1]
            newY[i] = y[pos-1]

        P = lagrange(newX, newY) if (metodo == 1) else newton(newX, newY)
        P.sort()
        print("Polinômio resultante: ",end = "")
        imprimePoly(P)
        print("\nDigite um ponto para ser avaliado ou uma letra para finalizar a avaliação: ", end="")
        eixoX = newX[:]
        while(True):
            try:
                t = input()
                print("P({}) = {}".format(float(t),calculaPonto(P,float(t))))
                if metodo != 1:
                    print("Erro : {}".format(erro(newX,matrizD(x,y),float(t))))
                eixoX += [float(t)]
            except ValueError:
                break

        #Definindo os eixos para impressão do gráfico
        eixoX.sort()
        n4 = len(eixoX)
        eixoY = [0]*n4
        eixoY = [ calculaPonto(P,eixoX[i]) for i in range(0,n4)]
        grafico(P,eixoX,eixoY)

        print("Deseja interpolar outro polinômio? y/n: ",end = "")
        t = input()
        if(t!='y'):
            break

main()

