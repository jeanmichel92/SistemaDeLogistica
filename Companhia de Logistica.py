#começo da função dimensoesObjeto#
def dimensoesObjeto():
    while True:
        try:
            comprimento = float(input("Digite o comprimento do objeto(em cm): "))
            largura = float(input("Digite a largura do objeto(em cm): "))
            altura = float(input("Digite a altura do objeto(em cm): "))
            volume = altura * comprimento * largura
            print("O volume do objeto é (em cm³): {:.2f}".format(volume))
            if volume < 1000:
                return 10
            elif 1000 <= volume < 10000:
                return 20
            elif 10000 <= volume < 30000:
                return 30
            elif 30000 <= volume < 100000:
                return 50
            elif volume >=100000:
                print("Não aceitamos objetos com dimensões tão grandes \nEntre com as dimensões desejadas novamente")
                continue
        except:
            print("Você digitou alguma dimensão do objeto com valor não numerico \nPor favor entre com as dimensões desejadas novamente")
            continue

#fim da função dimensoesObjeto#
#começo da função pesoObjeto#

def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto(em Kg): "))
            if peso <= 0.1:
                return 1
            elif 0.1 < peso <= 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            elif peso >= 30:
                print("Não aceitamos objetos tão pesados \nEntre com o peso desejado novamente")

        except ValueError:
            print("Você digitou peso do objeto com valor não numerico \nPor favor entre com o peso desejado novamente")
            continue

#fim da função pesoObjeto#
#inicio da função rotaObjeto#

def rotaObjeto():
    while True:
        print("\n BR - De Brasília para Rio de Janeiro\n BS - De Brasília para São Paulo\n "
                  "RB - De Rio de Janeiro para Brasília \n RS - De Rio de Janeiro para São Paulo\n "
                  "SR - De São Paulo para Rio de Janeiro \n SB - De São Paulo para Brasília \n")
        rota = str(input("Selecione a rota: >> "))

        if rota == "sr" or rota == "rs" or rota == "SR" or rota == "RS":
            return 1.0
        elif rota == "bs" or rota == "sb" or rota == "BS" or rota == "SB":
            return 1.2
        elif rota == "br" or rota == "rb" or rota == "BR" or rota == "RB":
            return 1.5
        else:
            print("Você digitou uma rota que não existe \nPor favor entre com a rota desejada novamente")


#fim da função rotaObjeto#

#começo da Main#
print("Bem vindo a Companhia de Logística Jean Michel Bete S.A.")
volume = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = volume * peso * rota

print("Total a pagar(R$): {} (dimensões: {} *  peso: {} * rota: {} )".format(total, volume, peso, rota))

#fim da Main#
