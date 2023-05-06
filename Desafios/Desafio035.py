segmento_01 = float(input("Digite o primeiro segmento: "))
segmento_02 = float(input("Digite o segundo segmento: "))
segmento_03 = float(input("Digite o terceiro segmento: "))

if segmento_01 < (segmento_02 + segmento_03) and segmento_02 < (segmento_01 + segmento_03) and segmento_03 <(segmento_01 + segmento_02):
    print("Os Segmentos acima PODEM FORMAR um triângulo!")
else:
    print("Os Segmentos acima NÃO PODEM FORMAR um triângulo!")
