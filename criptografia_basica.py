from random import shuffle, randint, seed

#Programa desenvolvido como exercício para o grupo de estudos
#que tem como propósito a prática de conceitos de programação
#através da criação de programas para solução de problemas.
#
#O seguinte módulo tem como objetivo tornar possível o processo
#de criptografia e descriptografia de mensagens simples. Para
#alcançar este objetivo, é feito o uso de peseudoaleatorieade da
#biblioteca random do python. 

def gerar_alfabeto(modo:str) -> dict:
    '''
    Cria um alfabeto de símbolos para realziar a criptografia e descriptografia de mensagens

    Descrição:

    Cria um dicionário referido como alfabeto que mapeia os símbolos aceitos em uma mensagem
    básica para outros símbolos que diferem do original e estão em conformidade com o modo
    passado para a função.

    Parâmetros:

    A função recebe como parâmetro o modo. Este é responsável por ditar o padrão
    utilizado para criar os símbolos para qual o caracteres de mensagem serão transformados.
    Os modos aceitos são:

    * p: Padrão - Gera valores que correspondem aos aceitos como símbolos de mensagem.
                  Estes são: Espaço em branco e caracteres alfabéticos (A-Z,a-z)
    
    * b: Binário - Gera valores que correspondem a números binários com tamanho fixo
                   de 6 dígitos. Estes são: números entre 000000 -  110100.
    
    * a: ASCII - Gera valores que correspondem a símbolos 'imprimíveis' da tabela ASCII.
                 Estes são: valores entre 32 - 126 (Representação Decimal)

    Retorno:

    Retorna um dicionário contendo chaves mapeadas para valores em conformidade
    ao modo informado como parâmetro.

    '''
    #Criação da lista que será usada como chaves em nosso alfabeto de símbolos
    chaves = [chr(32)] + [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
    
    #Verificação do modo de geração do alfabeto de símbolos

    if modo == "p":
        valores = chaves.copy()

    elif modo == "b":
        valores = []
        
        for i in range(0,53):
            binario = bin(i).replace("0b","")
            formatado = (6-len(binario))*"0" + binario
            valores.append(formatado)
 
    elif modo == "a":
        valores = [chr(i) for i in range(32,127)]

    #Embaralhamento dos valores - Gerar diferenciação pelo uso de 'aleatoriedade'
    shuffle(valores)
    alfabeto = {chaves[i]:valores[i] for i in range(len(chaves))}

    return alfabeto


def criptografar(mensagem:str, alfabeto:dict) -> str:
    '''
    Criptografa uma mensagem conforme um alfabeto de símbolos

    Descrição:

    Dada uma mensagem formada apenas por caracteres de mensagem válidos ( 
    espaços em brancos e caracteres alfabéticos A-Z,a-z), tem-se a mudança de seus caracteres 
    para outros símbolos conforme determinado pelo alfabeto de símbolos passado por parâmetro.
    O alfabeto de símbolos deve ser um dicionário cuja as chaves representam os caracteres
    de mensagem aceitos, e os valores representam os símobolos que serão usados no seu lugar
    no processo de criptografia. *Recomende-sa fortemente o uso da função gerar_alfabeto 
    (presente no mesmo módulo) para criação de um alfabeto válido*

    Parâmetros:

    - mensagem: Mensagem composto por espaços em brancos e caracteres alfabéticos A-Z,a-z
                que será criptografada

    - alfabeto: Dicionário que mapeia caracteres da mensagem para outros símbolos

    Retorno:

    Devolve uma mensagem criptografada a qual pode gerar a original através do uso
    da função de descriptografar (presente no mesmo módulo)
    '''

    mensagem_criptografada = ""

    for i in mensagem:
        mensagem_criptografada += alfabeto[i]

    return mensagem_criptografada


def descriptografar(mensagem:str, alfabeto:dict, modo:str) -> str:
    '''
    descriptografa uma mensagem conforme um alfabeto de símbolos

    Descrição:

    Dada uma mensagem criptografada, tem-se a mudança de seus símobolos para os caracteres originais
    conforme determinado pelo alfabeto de símbolos passado para a função de criptografia.
    O alfabeto de símbolos deve ser um dicionário cuja as chaves representam os caracteres
    de mensagem aceitos, e os valores representam os símobolos que foram usados no seu lugar
    no processo de criptografia. *Recomende-sa fortemente o uso das funções presentes neste módulo 
    para gerar um alfabeto de símbolos e criptografar uma mensagem de forma válida*

    Parâmetros:

    - mensagem: Mensagem criptografada com símbolos presentes no alfabeto informado

    - alfabeto: Dicionário que mapeia caracteres da mensagem original para os símbolos
                da mensagem criptografada. Deve corresponder ao mesmo dicionário utilizado
                no processo de criptografia, uma vez que este mapeia os caracteres de mensagem
                para os símbolos de criptografia.

    - modo: Modo utilizado na geração do alfabeto de símbolos que indica o padrão
            do alfabeto passado como parâmetro.

    Retorno:

    Devolve a mensagem criptografada de volta a sua forma original 
    '''
    passos = 1
    if modo == "b":
        passos = 6

    #Inversão do alfabeto de símbolos para facilitar o processo
    #de descriptografia através do uso de chave:valor dos dicionários
    alfabeto_inverso = {valor:chave for chave,valor in alfabeto.items()}
    mensagem_descriptografada = ""

    for i in range(0,len(mensagem),passos):
        elemento = mensagem[i:i+passos]
        mensagem_descriptografada += alfabeto_inverso[elemento]

    return mensagem_descriptografada


#Método principal do programa que faz o uso das funções anteriores
#para alcançar o objetivo proposto por este exercício. O ponto
#de destaque fica para o seed() - método da biblioteca random
#do python que gera uma sequencia pseudoaleatória por meio de uma valor -
#Que nos permite fazer uso da 'aleatorieade' para criar alfabetos e usa-los
#para criptografar e descriptografar uma mesma mensagem. Para mais detalhes,
#e um melhor entendimento do recurso utilizado neste programa, acesse a 
#documentação da biblioteca random em: https://docs.python.org/3/library/random.html
def main():
    executar = True
    while executar:
        print(" "*6000) 
        
        seed()

        #Menu
        print("-"*15)
        print("0 - Sair")
        print("1 - Criptografar Mensagem")
        print("2 - Descriptografar Mensagem")
        print("3 - Ajuda")
        print("-"*15)

        opcao = int(input("Digite a opção: "))

        if opcao == 0:
            executar = False
            break

        #Criptografar
        elif opcao == 1:
            print()
            print("1 - Gerar alfabeto com semente aleatoria")
            print("2 - Gerar alfabeto com semente determinada", end="\n"*2)

            op_criptografia = int(input("Informe a opção de criptografia: "))
            modo_criptografia = input("Informe o modo de criptografia: ")
            mensagem = input("Informe a mensagem: ")

            if op_criptografia == 1:
                semente = randint(1,1000000000000)
                seed(semente)
                alfabeto = gerar_alfabeto(modo_criptografia)

                print()
                print("Alfabeto: ",alfabeto)
                print("Semente:", semente) #Semente usada para gerar o alfabeto
                print("Mensagem criptografada:", criptografar(mensagem, alfabeto))

            elif op_criptografia == 2:
                semente = int(input("Informe a semente: "))
                seed(semente)

                alfabeto = gerar_alfabeto(modo_criptografia)
                print()
                print("Alfabeto: ",alfabeto)
                print("Semente:", semente)
                print("Mensagem criptografada:", criptografar(mensagem, alfabeto))

            else:
                print("Opção Inválida!")

        #Descriptografar
        elif opcao == 2:
            print()
            semente = int(input("Informe a semente para gerar o alfabeto: "))
            modo = input("Informe o modo da criptografia: ")
            mensagem = input("Informe a mensagem criptografada: ")
             
            
            seed(semente)
            alfabeto = gerar_alfabeto(modo)
            mensagem_descriptografada = descriptografar(mensagem, alfabeto, modo)

            print()
            print("Mensagem Descriptografada:", mensagem_descriptografada)

        #Informações para ajuda
        elif opcao == 3:
            print()
            print("Formato de mensagens aceitas:")
            print("  As mensagens que serão criptografadas podem somente conter")
            print("  Caracteres do tipo alfabético (a-z,A-Z) e espaço em branco")
            print()
            print("Modos de criptografia:")
            print("  O modo de criptografia determina o padrão de símbolos usadas")
            print("  devendo corresponder a:")
            print("  * p: Padrão - Corresponde aos caracteres aceitos no formato de mensagens")
            print("  * b: Binário - Corresponde aos números binários")
            print("  * a: ASCII - Corresponde aos símbolos 'imprimíveis' da tabela ASCII")
            print()
            print("Informações Relaventes:")
            print("  A Semente corresponde a um valor númerico <= 1000000000000")
            print("  que permite tanto o processo de criptografia, quanto de descriptografia.")
            print("  Está relacionada ao alfabeto de símbolos usado nestes processos e deve")
            print("  ser guardada para caso o usuário deseje descriptografar uma mensagem")
            print("  ou criptografar seguindo um padrão já conhecido.")
            

        else:
            print("Opção Inválida...")

        input("Pressione enter para continuar...")   

if __name__ == "__main__":
    main()