sequencia = 'ATGCGTACGTTAGCTAACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTATGCGTACGTTAGCTAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATATGCGTACGTTAGCTA'
primer = "ATGCGTACGTTAGCTA" 

#if primer in sequencia:
#    posicao = sequencia.find(primer)   
#    print(f"O primer foi encontrado na posição: {posicao + 1}")# Adiciona 1 para obter a posição correta (baseada em 1)
#else:
#    print("O primer não foi encontrado.")

contador = 0 # Contador para contar o número de ocorrências do primer
posicao = sequencia.find(primer) # Loop para encontrar todas as ocorrências do primer na sequência, limitando a 5 ocorrências

while (posicao != -1): # Verifica se o primer foi encontrado
    print(f"Ocorrência {contador + 1}: posição {posicao + 1}") # Adiciona 1 para obter a posição correta (baseada em 1)
    contador += 1 # Incrementa o contador
    posicao = sequencia.find(primer, posicao + 1) # Continua a busca a partir da posição seguinte à última ocorrência encontrada