vet_str = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def desconverte_str(s): #retorna o algarismo equivalente em decimal caso a base seja maior 
    for i in range(0, len(vet_str)):
        if(s == vet_str[i]):
            return i + 10

def converte_em_str(n): #retorna o algarismo equivalente caso a base seja maior que a decimal
    for i in range(0, len(vet_str)):
        if(n == i + 10):
            return vet_str[i] 

def dec_to_base(n, base_destino): 
    atual = n
    result = ''

    while(atual > (base_destino - 1)):  #verifica se ainda e possivel realizar divisoes inteiras
        resto = atual % base_destino

        if(resto > 9):  #verifica se e necessario converter o resto em algum algarismo de uma base maior que a decimal          
            resto = converte_em_str(resto) 

        result = result + str(resto) #concatena os restos
        atual = atual//base_destino #atualiza o valor do novo dividendo

    if(atual > 9):
        atual = converte_em_str(atual) #verifica se e necessario converter o ultimo quaciente em algum algarismo de uma base maior que a decimal

    result = result + str(atual) 
    return result[::-1] #reverte a ordem dos algarismo, fazendo com que o numero inicie pelo algarismo mais significativo

def base_to_dec(n, base_origem):
    result = 0
    n = str(n)[::-1] #inverte a ordem dos algarismos de modo que a multiplicacao pelo menor expoente comece pelo algarismo menos significativo
    exp_base = 0

    for algarismo in n:
        if(algarismo in vet_str): #verifica se e necessario fazer a conversao do algarismo de letra para numero
            algarismo =  desconverte_str(algarismo)
        
        result = result + (int(algarismo) * (base_origem** exp_base)) #soma o resultado as sucessivas multiplicacoes
        exp_base = exp_base + 1
    
    return result

numero = input("Digite o numero: ")
base_origem = input("Digite a base atual: ")
base_destino = input("Digite a base desejada: ")

if(base_origem==''): #caso a base de origem nao seja informada, ela sera tida como 10
    base_origem = 10
if(base_destino==''): #caso a base de destino nao seja informada, ela sera tida como 10
    base_destino = 10

base_origem = int(base_origem) #passagem do tipo string para o tipo inteiro
base_destino = int(base_destino)

if(base_origem == base_destino):
    print(f"{numero} na base {base_origem}")
else:
    if(base_origem <= 10):
        numero = int(numero)
    if(base_origem == 10):
        print(f"Resultado = {dec_to_base(numero, base_destino)} na base {base_destino}.")
    elif(base_destino == 10):
        print(f"Resultado = {base_to_dec(numero, base_origem)} na base 10.")
    else:
        decimal = base_to_dec(numero, base_origem) #caso nem a base de origem nem a de destino sejam 10, o numero sera primeiramente convetido pra a base 10
        print(f"Resultado = {dec_to_base(decimal, base_destino)} na base {base_destino}.")

