peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"O seu IMC é de {imc:.1f} e você está ABAIXO do peso!")
elif imc < 25:
    print(f"O seu IMC é de {imc:.1f} e você está no seu peso IDEAL!")
elif imc < 30:
    print(f"O seu IMC é de {imc:.1f} e você está com SOBREPESO!")
elif imc < 40:
    print(f"O seu IMC é de {imc:.1f} e você está com OBESIDADE!")
elif imc > 40:
    print(f"O seu IMC é de {imc:.1f} e você está com OBESIDADE MÓRBIDA!")
