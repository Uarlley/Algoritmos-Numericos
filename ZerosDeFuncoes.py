maxIteracoes = 100

class Polinomio:
    def __init__(self, grau, coef):
        self.grau = grau
        self.coef = coef

    def __lt__(self, other):
        return (self.grau >= other.grau)


def f(ponto, x):
    r = 0
    n = len(x)
    for i in range(0, n):
        r += x[i].coef * (ponto ** (x[i].grau))
    return r


def lePolinomio():
    print("Digite o grau do polinomio: ", end="")
    n = int(input()) + 1
    x = []
    for i in range(n - 1, -1, -1):
        if (i != 0):
            print("Digite o coeficiente de x^({}):".format(i), end="")
        else:
            print("Digite o coeficiente do termo idependente: ", end="")

        coeficiente = float(input())
        aux = Polinomio(i, coeficiente)
        x += [aux]

    x.sort()
    return x


def copiaPolinomio(x):
    copia = []
    n = len(x)
    for i in range(0, n):
        coeficiente = x[i].coef
        grau = x[i].grau
        aux = Polinomio(grau, coeficiente)
        copia += [aux]
    return copia


def calculaDerivada(x):
    n = len(x)
    for i in range(0, n):
        if (x[i].grau != 0):
            x[i].coef *= x[i].grau
            x[i].grau -= 1
        else:
            x[i].coef = 0
    return x


def imprimePoly(x):
    n = len(x)
    for i in range(0, n):

        if (i != 0 and x[i].coef > 0):
            print(" +", end="")

        if (x[i].coef != 0):
            if (x[i].grau == 0):
                print(" {}".format(x[i].coef), end="")

            if (x[i].grau == 1):
                print(" {}x".format(x[i].coef), end="")

            if (x[i].grau > 1):
                print(" {}x^({}) ".format(x[i].coef, x[i].grau), end="")

    print()


def bissecao(g, a, b, episilon, i=1, l=[], e=[]):
    if i <= maxIteracoes:
        x1 = (a + b) / 2
        erro = abs((a - b) / 2)
        if erro < episilon:
            return l + [x1], e + [erro]
        elif f(a, g) * f(x1, g) < 0:
            b = x1
            return bissecao(g, a, b, episilon, i + 1, l + [x1], e + [erro])
        elif f(b, g) * f(x1, g) < 0:
            a = x1
            return bissecao(g, a, b, episilon, i + 1, l + [x1], e + [erro])
        return l + [x1], e + [erro]
    else:
        return l, e


def newtonraphson(g, g_linha, x1, episilon, i=1, l=[], e=[]):
    if i <= maxIteracoes:
        if f(x1, g) != 0:
            x2 = x1 - (f(x1, g) / f(x1, g_linha))
            erro = abs((x2 - x1) / x2)
            if (erro < episilon):
                return l + [x2], e + [erro]
            else:
                return newtonraphson(g, g_linha, x2, episilon, i + 1, l + [x2], e + [erro])
        else:
            return l, e
    else:
        return l, e


def secante(g, x1, x2, episilon, i=1, l=[], e=[]):
    if i <= maxIteracoes:
        if (f(x2, g) - f(x1, g)) != 0:
            x = x2 - ((f(x2, g) * (x2 - x1)) / (f(x2, g) - f(x1, g)))
            erro = abs((x - x2) / x)
            if erro < episilon:
                return l + [x], e + [erro]
            else:
                x1 = x2
                x2 = x
                return secante(g, x1, x2, episilon, i + 1, l + [x], e + [erro])
        else:
            return l, e


def imprimeAux(val):
    if (val >= 0):
        if(val >= 10):
            print(" {:.15f}  |".format(val), end="")
        else:
            print("  {:.15f}  |".format(val), end="")
    else:
        if(abs(round(val, 14)) >= 10):

            print("{:.15f}  |".format(val), end="")
        else:
            print(" {:.15f}  |".format(val), end="")


def imprime_resultado(apro, erro, g):
    n = len(apro)
    print("\n\n|----------|---------------------|---------------------|---------------------|")
    print("| Iteração |          x          |        f(x)         |         erro        |")
    for i in range(0, n):
        print("|    {:02.0f}    |".format(i + 1), end="")
        imprimeAux(apro[i])
        imprimeAux(f(apro[i], g))
        imprimeAux((erro[i]))
        print()

    print("|----------|---------------------|---------------------|---------------------|\n\n")


def main():
    g = lePolinomio()
    g_linha = calculaDerivada(copiaPolinomio(g))
    print("\nf(x) : ", end = "")
    imprimePoly(g)
    print("f'(x) = ", end = "")
    imprimePoly(g_linha)
    while (True):
        print("\n|--------------|")
        print("| 1 - Bisseção |")
        print("| 2 - Secante  |")
        print("| 3 - Newton   |")
        print("|--------------|", end="\n\n")

        try:
            op = int(input("Digite qual dos métodos deseja utilizar ou uma letra para finalizar a execução: "))
            episilon = float(input("Digite o valor de episilon: "))
            if (op == 1):
                a = float(input("Digite o interválo\n   a: "))
                b = float(input("   b: "))
                aprox, erro = bissecao(g, a, b, episilon)
                imprime_resultado(aprox, erro, g)

            elif (op == 2):
                x1 = float(input("Digite o interválo\n   x1: "))
                x2 = float(input("   x2: "))
                aprox, erro = secante(g, x1, x2, episilon)
                imprime_resultado(aprox, erro, g)

            elif (op == 3):
                x1 = float(input("Digite o valor do ponto inicial x1: "))
                aprox, erro = newtonraphson(g, g_linha, x1, episilon)
                imprime_resultado(aprox, erro, g)
            else:
                print("Opção inválida!")

        except ValueError:
            print("Fim da execução")
            break


main()
