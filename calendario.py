def verificar_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

#Acha o dia da semana para qualquer dia, mes e ano informado.
#Retorno possível: 0,1,2,3,4,5,6 onde cada valor corresponde:
#0 -> Sábado; 1 -> Domingo; 2 -> Segunda-Feira; [...] ; 6 -> Sexta-Feira
#Para mais informações pesquise pela Congruência de Zeller e sua implementação em Software    
def calcular_congruencia_zeller(dia,mes,ano):  
    if mes == 1: 
        mes = 13
        ano -= 1  

    if mes == 2: 
        mes = 14
        ano -= 1
 
    k = ano%100; 
    j = ano//100; 
    ds = (dia + ((13*(mes + 1))//5) + k + (k//4) + (j//4) + (5*j))%7
    return ds

#Formatação do retorno dado pela função calcular_congruencia_Zeller
#Formata para que o valor seja melhor aproveitado para a exibição do calendário
dia_formatado = {0:6,1:0,2:1,3:2,4:3,5:4,6:5}

qtd_dias_por_mes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,10:31,11:30,12:31}

mes = {1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho",
         7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}

ano = int(input("Digite o ano que deseja gerar o calendario: "))
if verificar_bissexto(ano):
    qtd_dias_por_mes[2] = 29

for i in range(1,13):
    #Ordem é a formatação do primeiro dia de cada mês(representado pela variavel i no laço for) do ano solicitado
    ordem = dia_formatado[calcular_congruencia_zeller(1,i,ano)]
    print("-"*10)
    print(mes[i])
    print()
    print("Dom Seg Ter Qua Qui Sex Sab")
    #Espaçamentos para que o mês inicie no dia da semana correto. Cada espaçamento tem tamanho 4 (4 espaços)
    print("    "*ordem, end="")

    for x in range(1,qtd_dias_por_mes[i]+1):
        #Verifica se a soma da qtd de espaçamentos com dia atual é multiplo de 7(disposição dos numeros em um calendário, 
        #conforme o calculo de semana) para marcar uma semana
        if (x+ordem)%7 == 0:
            print(x, end="\n")
        else:
            print(x, end=" "*(4-(len(str(x)))))
    print()
    print()