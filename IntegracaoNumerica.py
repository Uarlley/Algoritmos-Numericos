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


def calculaDerivada(x):
    n = len(x)
    for i in range(0, n):
        if (x[i].grau != 0):
            x[i].coef *= x[i].grau
            x[i].grau -= 1
        else:
            x[i].coef = 0
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


def imprimeAux(val):
    if (val >= 0):
        if (val >= 10):
            print(" {:.15f}  |".format(val), end="")
        else:
            print("  {:.15f}  |".format(val), end="")
    else:
        if (abs(round(val, 14)) >= 10):

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


def exato(g, a, b):
    n = len(g)
    for i in range(0, n):
        g[i].grau += 1
        g[i].coef /= (g[i].grau)
    return f(b, g) - f(a, g)


def simpson38(g, g_d, a, b, m):
    calculaDerivada(g_d)
    h = (b-a)/m
    soma = 0
    x = [a + h*i for i in range(0, m+1)]
    print(x)
    fi = max([f(x[i], g_d) for i in range(1, m)])
    erro = (-1)*((b-a)**5)/(80*(m**4))*fi
    for i in range(0, m+1):
        if(i == 0 or i == m):
            soma += f(x[i], g)
        else:
            soma += 2*f(x[i], g) if i % 3 == 0 else 3*f(x[i], g)

    soma *= (3*h)/8
    return soma, abs(erro)


def simpson13(g, g_d, a, b, m):
    calculaDerivada(g_d)
    h = (b-a)/m
    soma = 0
    x = [a + h*i for i in range(0, m+1)]
    fi = max([f(x[i], g_d) for i in range(1, m)])
    erro = (-1)*((b-a)**5)/(180*(m**4))*fi
    for i in range(0, m+1):
        if(i == 0 or i == m):
            soma += f(x[i], g)
        else:
            soma += 2*f(x[i], g) if i % 2 == 0 else 4*f(x[i], g)
    soma *= h/3
    return soma, abs(erro)


def trapeziosRepetidos(g, g_d, a, b, m):
    soma = 0
    h = (b - a) / m
    fi = []
    for i in range(0, m + 1):
        print(a,end = ", ")
        fi += [f(a, g_d)]
        soma += f(a, g) if (i == 0 or i == m) else 2 * f(a, g)
        a += h

    erro = (-1) * ((b - a) ** 3) / (12 * m ** 2) * (abs(max(fi, key=abs)))
    soma *= h / 2

    return soma, abs(erro)


def main():
    g = lePolinomio()
    g_d = calculaDerivada(copiaPolinomio(calculaDerivada(copiaPolinomio(g))))

    print("\nF(x) = ", end = "")
    imprimePoly(g)
    a = float(input("\nDigite o interválo\n\ta: "))
    b = float(input("\tb: "))
    while (True):
        print("|----------------------------|")
        print("| 1 - Trapézios Repetidos    |")
        print("| 2 - 1/3 Simpson Repetidos  |")
        print("| 3 - 3/8 Simpson Repetidos  |")
        print("|----------------------------|", end="\n\n")

        try:
            op = int(input("Qual método deseja utilizar ou uma letra para finalizar a execução: "))
            if (op == 1):
                m = int(input("Digite o número de subinterválos: "))
                resultado, erro = trapeziosRepetidos(g, g_d, a, b, m)
                print("\n\tResultado da aproximação: ", resultado)
                print("\tErro: ", erro)

            elif (op == 2):
                m = int(input("Digite um número par de subinterválos: "))
                if(m % 2 == 0):
                    resultado, erro = simpson13(g, calculaDerivada(copiaPolinomio(g_d)), a, b, m)
                    print("\n\tResultado da aproximação: ", resultado)
                    print("\tErro: ", erro)

                else:
                    print("\tEntrada inválida!")

            elif (op == 3):
                m = int(input("Digite um número de subinterválos multiplo de 3: "))
                if(m % 3 == 0):
                    resultado, erro = simpson38(g, calculaDerivada(copiaPolinomio(g_d)), a, b, m)
                    print("\n\tResultado da aproximação: ", resultado)
                    print("\tErro: ", erro)

                else:
                    print("\tEntrada inválida!")

            else:
                print("Opção inválida!")

            print("\tValor da integral utilizando o TFC (Teorema Fundamental do Cálculo): ",
                  exato(copiaPolinomio(g), a, b), "\n")

        except ValueError:
            print("Fim da execução")
            break


main()
