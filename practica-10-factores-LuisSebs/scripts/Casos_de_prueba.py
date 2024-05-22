from Factores import Variable, Factor

if __name__ == "__main__":

    # Ejemplos del pdf (imagenes)

    # a) Creacion de factores f1 y f2
    A = Variable('A', [1,2])
    B = Variable('B', [5,10,15])
    C = Variable('C', [1,2,3])

    f1 = Factor((A,), [1,2])
    f2 = Factor((B,C),[5,10,15,10,20,30,15,30,45])

    print("Factor 1")
    print("Variables: ")
    print("------------------")
    for v in f1.alcance:
        print(v)
    print("------------------")
    print(f1)

    print("Factor2")
    print("Variables: ")
    print("------------------")
    for v in f2.alcance:
        print(v)
    print("------------------")
    print(f2)

    # b) Multiplicando f1 y f2, para obtener

    f3 = f1.multiply(f2)

    print("Multiplicando f1 y f2: f3")
    print("Variables:")
    print("------------------")
    for v in f3.alcance:
        print(v)
    print("------------------")
    print(f3)

    # c) Normalizando f3

    f3_n = f3.normalize()

    print("Normalizando el resultado de la multiplicacion")
    print("Variables:")
    print("------------------")
    for v in f3_n.alcance:
        print(v)
    print("------------------")
    print(f3_n)

    # d) Reduciendo y marginalizando

    f3_nrA = f3_n.reduce(A,1)
    f3_mB = f3_n.marginalize(B)

    print("Reduciendo la variable A con valor 1 de f3")
    print("Variables:")
    print("------------------")
    for v in f3_nrA.alcance:
        print(v)
    print("------------------")
    print(f3_nrA)
    print("Marginalizando la variable B de f3")
    print("Variables")
    print("------------------")
    for v in f3_mB.alcance:
        print(v)
    print("------------------")
    print(f3_mB)