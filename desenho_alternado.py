n = 2
while n%2 == 0:
    n = int(input("Digite um numero de linhas impar: "))

desenho = []
car = ""

car1 = input("Digite um caractere para ser usado no desenho: ")
car2 = input("Agora digite outro caractere para o mesmo proposito: ")

for linha in range(n):
    desenho.append([])
    for coluna in range(n):
        desenho[linha].append("")

for contador in range(n//2+1):
	if contador%2 == 0:
		car = car1
	else:
		car = car2

	for linha in range(0+contador,n-contador):
		for coluna in range(0+contador,n-contador):
			desenho[linha][coluna] = car

for linha in range(n):
    print()
    for coluna in range(n):
        print(desenho[linha][coluna], end=" ")

print()    
