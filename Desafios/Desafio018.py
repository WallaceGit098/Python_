from math import radians,cos,sin,tan

angulo = float(input("Digite o Ângulo desejado: "))

cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print(f" O Cosseno de {angulo} é {cosseno:.2f}\n O Seno de {angulo} é {seno:.2f}\n A Tangente de {angulo} é {tangente:.2f}")