r1 = float(input("Digite o primeiro lado: "))
r2 = float(input("Digite o segundo lado: "))
r3 = float(input("Digite o terceiro lado: "))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1+r2):
    if r1 == r2 == r3:
        print("Os Segmentos PODEM formar um triângulo e o triângulo formado é Equilátero!")
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("Os Segmentos PODEM formar um triângulo e o triângulo formado é Isósceles")
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print("Os Segmentos PODEM formar um triângulo e o triângulo formado é Escaleno!")
else:
    print("Os segmentos a cima não podem formar um triângulo!")
