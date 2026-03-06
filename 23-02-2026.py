levantamento = [
    "Melipona scutellaris",
    "Scaptotrigona postica",
    "Tetragonisca angustula",
    "Melipona scutellaris",
    "Scaptotrigona postica",
    "Scaptotrigona depilis",
    "Melipona quadrifasciata",
    "Friesiomelita varia",
    "Scaptotrigona postica"
]
# 1)
print("========Ninhos observados========")9
for i, ninho in enumerate(levantamento, start=1): #Usar a função enumerate() para iterar sobre a lista levantamento
    print(f"{i}. {ninho}")

# 2) 
total_ninhos = len(levantamento) #Calcular o total de ninhos usando a função len() para obter o número de elementos na lista levantamento
print(f"\nTotal de ninhos observados: {total_ninhos}")

# 3) 
from collections import Counter #Importar a classe Counter do módulo collections (biblioteca padrão do Python)
contador_especies = Counter(levantamento) 
print("\n========Número de ninhos por espécie========") 
for especie, quantidade in contador_especies.items(): 
    print(f"{especie}: {quantidade}")

# 4) 
contador_generos = Counter(ninho.split()[0] for ninho in levantamento) #Criar um contador, extraindo o primeiro elemento de cada nome usando uma compreensão de lista
print("\n========Número de ninhos por gênero========")
for genero, quantidade in contador_generos.items():
    print(f"{genero}: {quantidade}")

