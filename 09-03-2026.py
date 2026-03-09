sequencia = 'ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTATGCGTACGTTAGCTAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGAT'
primer = "ATGCGTACGTTAGCTA" 

if primer in sequencia:
    posicao = sequencia.find(primer) + 1  # Adiciona 1 para obter a posição correta (baseada em 1)
    print(f"O primer foi encontrado na posição: {posicao}")
else:
    print("O primer não foi encontrado.")
