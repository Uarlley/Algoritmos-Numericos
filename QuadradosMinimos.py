import matplotlib.pyplot as plt
import numpy as np

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


#funcao que cria um polinomio de grau 1, definido por (ax + b)
def criaPoly(coef, ponto):
    return [Polinomio(1,coef),Polinomio(0, ponto)]

#funco que multiplica o polinomio por uma constante
def  multPorConstante(constante,lista):
    n = len(lista)
    for i in range(0,n):
        lista[i].coef *= constante
    return lista


#funcao que calcula os quadrados minimos
def quadradosMinimos(x,y):
    n = len(x)
    s1 = s2 = s3 = s4 = 0
    for i in range(0,n):
        s1 += x[i]
        s2 += y[i]
        s3 += x[i]*y[i]
        s4 += x[i]*x[i]

    a = (s1*s2 - n*s3)/(s1*s1 -n*s4)
    return a,(s2 - a*s1)/n

#funcao que mostra graficamente os pontos fornecidos
def pontos(x,y):
    fig, ax = plt.subplots(figsize=(10, 5))

    n = len(x)
    for i in range(0,n):
        plt.plot(x[i], y[i], color='#1F77B4', marker='o', lw=2, markersize=8,
                 markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')
    ax.yaxis.grid(True, linestyle='-', which='major', color='#85878b', alpha=1.0)
    ax.xaxis.grid(True,linestyle='-', which='major', color='#85878b', alpha=1.0)
    fontSize = 12
    ax.set_axisbelow(True)

    plt.xticks(np.arange(min(x)-1, max(x) + 1, 0.5))
    plt.yticks(np.arange(min(y)-1, max(y) + 1, 0.5))

    plt.show()
    plt.tight_layout()
    plt.close()

#funcao que mostra o grafico do polinomio resultante
def grafico(polinomio,x,y):

    fig, ax = plt.subplots(figsize=(10, 5))
    text = "$"
    for i in range(0,2):
        if(polinomio[i].coef != 0):
            if(i != 0 and polinomio[i].coef > 0):
                text += "+"
            text += str(round(polinomio[i].coef,4))
            if(polinomio[i].grau) > 1:
                text += "x^{" + str(polinomio[i].grau) + "}"
            if(polinomio[i].grau) == 1:
                text += "x"
    text += "$"

    n = len(x)
    for i in range(0,n):
        plt.plot(x[i], y[i], color='#1F77B4', marker='o', lw=2, markersize=8,
                 markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')


    plt.plot([x[0],x[n-1]], [calculaPonto(polinomio,x[0]),calculaPonto(polinomio,x[n-1])], label= text, color='#1F77B4')

    ax.yaxis.grid(True, linestyle='-', which='major', color='grey', alpha=1.0)
    ax.xaxis.grid(True,linestyle='-', which='major', color='grey', alpha=1.0)


    fontSize = 12
    ax.set_axisbelow(True)
    plt.xticks(np.arange(min(x)-1, max(x) + 1, 0.5))
    plt.yticks(np.arange(min(y)-1, max(y) + 1, 0.5))
    leg = plt.legend(fontsize=fontSize)

    leg.set_title('', prop={'size': fontSize + 2})

    plt.show()
    plt.tight_layout()
    plt.close()

def D(u,y):
    a = 0
    n = len(u)
    for i in range(0,n):
        a += (u[i]-y[i])**2
    return a

def qualidadeDoAjuste(a,b,x,y):
    s1 = s2 = 0
    n = len(x)
    for i in range(0,n):
        s1 = (y[i] - b - a*x[i])**2
        s2 = y[i]*y[i]

    return 1 - (s1/(s2-(1/n)*s2*s2))

def main():

    #definição dos pontos
    x = [0.3, 2.7, 4.5, 5.9, 7.8]

    # Definindo os valores do vetor y
    y = [1.8, 1.9, 3.1, 3.9, 3.3]

    pontos(x,y)
    n = len(x)
    a,b = quadradosMinimos(x,y)
    polinomio  = criaPoly(a,b)
    print("Função resultante: ",end = "")
    imprimePoly(polinomio)
    grafico(polinomio,x,y)
    print("Digite um ponto para ser avaliado ou uma letra para finalizar a avaliação: ", end="")
    while (True):
        try:
            t = input()
            print("u({}) = {}".format(float(t), calculaPonto(polinomio, float(t))))
        except ValueError:
            break
    u = [calculaPonto(polinomio,x[i]) for i in range(0,n)]
    d = D(u,y)
    print("Desvio: {}".format(d))
    print("Qualidade do Ajuste: ", qualidadeDoAjuste(a,b,x,y))

main()