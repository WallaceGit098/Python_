print("---CHURRASCANÇA BAR---")
print("1 - Johnnie Walker")
print("2 - Chivas")
print("3 - Jack Daniels")
print("4 - Bourbons")
print("0 - Sair")

marca= int(input("""
Qual marca você deseja? """))

if marca == 1:
    print("1 - Red Label - R$ 99,90")
    print("2 - Black Label - R$ 109,99")
    print("3 - Green Label - R$ 209,90")
    print("4 - Blue Label - R$ 599,90 ")

    jw= int(input("Qual será o whisky escolhido dentro da marca Johnnie Walker? "))
    
    if jw == 1:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Red Label, deseja confirmar sua escolha? "))
        
        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 99.90:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 99.90:
                troco = dinheiro - 99.90
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

            else: 
                print("Opção inválida")
            #opção invalida

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")
       #if confirmação == 1: encerrar / == 2: voltar para o menu anterior

    elif jw == 2:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Black Label, deseja confirmar sua escolha? "))

        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 109.99:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 109.99:
                troco = dinheiro - 109.99
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")

    elif jw == 3:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Green Label, deseja confirmar sua escolha? "))

        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 209.90:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 209.90:
                troco = dinheiro - 209.90
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")
            
    elif jw == 4:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Blue Label, deseja confirmar sua escolha? "))

        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 599.90:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 599.90:
                troco = dinheiro - 599.90
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")

    else:
        print("Opção inválida")

elif marca == 2:
    print("1 - Chivas 12 anos - R$112,90")
    print("2 - Chivas 18 anos - R$239,90")
    print("3 - Chivas 22 anos - R$579,00")
          
    jw= int(input("Qual será o whisky escolhido dentro da marca Chivas? "))
    
    if jw == 1:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Chivas 12 anos, deseja confirmar sua escolha? "))
        
        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 112.90:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 112.90:
                troco = dinheiro - 112.90
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

            else: 
                print("Opção inválida")
            

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")
       #if confirmação == 1: encerrar / == 2: voltar para o menu anterior

    elif jw == 2:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Chivas 18 anos, deseja confirmar sua escolha? "))

        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 239.90:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 239.90:
                troco = dinheiro - 239.90
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")

    elif jw == 3:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Chivas 22 anos, deseja confirmar sua escolha? "))

        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 579.00:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 579.00:
                troco = dinheiro - 579.00
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")

elif marca == 3:
    print("Maçã Verde - R$112,90")
    print("Mel - R$160,90")
    print("Classic Jack - R$1000,00")

    jw= int(input("Qual será o whisky escolhido dentro da marca Johnnie Walker? "))

    if jw == 1:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Jack Daniels Green Apple, deseja confirmar sua escolha? "))
        
        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 112.90:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 112.90:
                troco = dinheiro - 112.90
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

            else: 
                print("Opção inválida")
            #opção invalida

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")
       #if confirmação == 1: encerrar / == 2: voltar para o menu anterior

    elif jw == 2:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Jack Daniels Honey, deseja confirmar sua escolha? "))

        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 160.90:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 160.90:
                troco = dinheiro - 160.90
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! : ")

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")

    elif jw == 3:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Classic Jack, deseja confirmar sua escolha? "))

        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 1000.00:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 1000.00:
                troco = dinheiro - 1000.00
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")

elif marca == 4:
    print("Ballantines - R$110,00 ")
    print("Buchanans - R$125,00")

    jw= int(input("Qual será o whisky escolhido dentro da marca Johnnie Walker? "))
    
    if jw == 1:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Ballantines Bourbon, deseja confirmar sua escolha? "))
        
        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 110.00:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 110.00:
                troco = dinheiro - 110.00
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

            else: 
                print("Opção inválida")
            #opção invalida

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")
       #if confirmação == 1: encerrar / == 2: voltar para o menu anterior

    elif jw == 2:
        print("1 - Sim\
               2 - Não")
        confirmação= int(input("O Whisky escolhido foi Buchanans Bourbon, deseja confirmar sua escolha? "))

        if confirmação == 1:
            dinheiro = float(input("Digite a quantia de dinheiro entregue: "))
            
            if dinheiro < 125.00:
                print ("A compra não pode ser confirmada devido a falta de saldo.")

            elif dinheiro >= 125.00:
                troco = dinheiro - 125.00
                print("O seu troco foi: {:.2f}".format(troco))
                print("A compra foi realizada com sucesso! :)")

        if confirmação == 2:
            print("Iremos te redirecionar para o menu anterior.")

    else:
        print("Opção inválida")

elif marca == 0:
    print("O programa será encerrado!")

else:
    print("Opção inválida")