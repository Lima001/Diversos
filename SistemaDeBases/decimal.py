#Simbolos para permitir a entrada de numeros até a base 36
#Para ampliar as bases suportadas pelo programa, basta adicionar mais elementos ao dicionario
#de simbolos

simbolos = {
    "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10,
    "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20, "L":21,
    "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29 ,"U":30, "V":31 ,"W":32,
    "X":33, "Y":34, "Z":35
}

#Dicionario utilizado para converter digitos decimais para outras bases
#Segue o mesmo esquema do dicionário anterior, visto que é é constituido
#Da inversão de chave:valor
simbolos_invertidos = {chave:valor for valor,chave in simbolos.items()}

def gerar_decimal(num,base):
    decimal = 0
    num = list(str(num))
    for i in range(len(num)):
        decimal += int(simbolos[num[-1-i].upper()])*(base**i)
    return decimal

def converter_decimal(num,base):
    saida = ""
    exe = True
    while exe:
        if num < base:
            exe = False
        resto = num % base
        num = num // base
        saida += simbolos_invertidos[resto]
    return saida[-1::-1]

if __name__ == "__main__":

    exe = True
    while exe:
        print("\n"*100)
        print("-- Menu --")
        print("1 - Converter de alguma base para decimal")
        print("2 - Converter de decimal para outra base")
        print("3 - Sair\n")
        op = int(input("Digite a opção: "))
    
        if op == 1:
            ope = True
            while ope:
                base = int(input("Digite a base de saída (2-36): "))
                if base > 1 and base <= 36:
                    ope = False
                num = input("Digite o numero para converter: ")
                print(gerar_decimal(num,base))

        elif op == 2:
            ope = True
            while ope:
                base = int(input("Digite a base de saída (2-36): "))
                if base > 1 and base <= 36:
                    ope = False
                num = int(input("Digite o numero para decimal: "))
                print(converter_decimal(num,base))
        
        elif op == 3:
            exe = False
        
        else:
            print("Opção inválida")
    
        trava = input("\nPrecione Enter para prosseguir")