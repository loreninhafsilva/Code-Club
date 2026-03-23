#Modo mais simples
sequencia = "GTCGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTATCGAGTTTTGAAACGGGTTGTAGCTGGCCTTCCGAGGCATGTGCACGCCCTGCTCATCCACTCTACACCTGTGCACTTACTGTAGGCTTTCGGGAGCTTCGAAAGCAGAGGGGACTTGGCCTTCACAAGCCGAGTCTCTAATGCCTGTAGTTGTGACCGGGGCTTACGTCTTACCACAAACTCTTATAAAGTATCAGAATGTGTATTGCGATGTAACGCATCTATATACAACTTTCAGCAACGGATCTCTTGGCTCTCGCATCGATGAAGAACGCAGCGAAATGCGATAAGTAATGTGAATTGCAGAATTCAGTGAATCATCGAATCTTTGAACGCACCTTGCGCTCCTTGGTATTCCGAGGAGCATGCCTGTTTGAGTGTCATGAAATTCTCAACCTAACGGGTTCTTAACGGGACTTGCTTAGGCTTGGACTTGGAGGCTTGTCGGCTTTGCTCTGCATAAGTCGGCTCCTCTCAAATGCATTAGCTTGGTTCCTTGCGGATCGGCTCACGGTGTGATAATTGTCTACGCCGCGACCGTTGAAGCGTTTTAATGGGCCAGCTTCTAATCGTCTCTTGCGAGACAACATTCATCGAACTCTGACCTCAAATCAGGTAGGACTACCCGCTGAACTT"

#1️ Tamanho da sequência
tamanho = len(sequencia)
print(f"Tamanho da sequência: {tamanho}")

#2️ Número de vezes que aparece a base C
num_c = sequencia.count('C')
print(f"Número de vezes que aparece a base C: {num_c}")

#3️ Número de vezes que aparece a base G
num_g = sequencia.count('G')
print(f"Número de vezes que aparece a base G: {num_g}")

#4️ Porcentagem de C G
total_bases = num_c + num_g
porcentagem_cg = (total_bases / tamanho) * 100
print(f"Porcentagem de C e G: {porcentagem_cg:.2f}%")

#Modo mais complexo

def analisar_sequencia(sequencia: str) -> dict:
    sequencia = sequencia.upper().strip()
    bases_validas = set('ATCG')
    
    if not sequencia:
        raise ValueError("Sequência vazia!")
    if not set(sequencia).issubset(bases_validas):
        invalidas = set(sequencia) - bases_validas
        raise ValueError(f"Bases inválidas encontradas: {invalidas}")
    
    tamanho = len(sequencia)
    contagem = {base: sequencia.count(base) for base in 'ATCG'}
    total_cg = contagem['C'] + contagem['G']
    
    return {
        "tamanho": tamanho,
        "contagem": contagem,
        "porcentagem_cg": (total_cg / tamanho) * 100,
        "porcentagem_at": ((contagem['A'] + contagem['T']) / tamanho) * 100,
    }

def exibir_resultados(resultado: dict):
    print(f"{'='*40}")
    print(f"  ANÁLISE DA SEQUÊNCIA DE DNA")
    print(f"{'='*40}")
    print(f"  Tamanho total:       {resultado['tamanho']} bases")
    print(f"{'─'*40}")
    print(f"  Contagem por base:")
    for base, qtd in resultado['contagem'].items():
        pct = (qtd / resultado['tamanho']) * 100
        print(f"    {base}: {qtd:>4}  ({pct:.1f}%)")
    print(f"{'─'*40}")
    print(f"  Conteúdo GC:  {resultado['porcentagem_cg']:.2f}%")
    print(f"  Conteúdo AT:  {resultado['porcentagem_at']:.2f}%")
    print(f"{'='*40}")

sequencia = "GTCGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTATCGAGTTTTGAAACGGGTTGTAGCTGGCCTTCCGAGGCATGTGCACGCCCTGCTCATCCACTCTACACCTGTGCACTTACTGTAGGCTTTCGGGAGCTTCGAAAGCAGAGGGGACTTGGCCTTCACAAGCCGAGTCTCTAATGCCTGTAGTTGTGACCGGGGCTTACGTCTTACCACAAACTCTTATAAAGTATCAGAATGTGTATTGCGATGTAACGCATCTATATACAACTTTCAGCAACGGATCTCTTGGCTCTCGCATCGATGAAGAACGCAGCGAAATGCGATAAGTAATGTGAATTGCAGAATTCAGTGAATCATCGAATCTTTGAACGCACCTTGCGCTCCTTGGTATTCCGAGGAGCATGCCTGTTTGAGTGTCATGAAATTCTCAACCTAACGGGTTCTTAACGGGACTTGCTTAGGCTTGGACTTGGAGGCTTGTCGGCTTTGCTCTGCATAAGTCGGCTCCTCTCAAATGCATTAGCTTGGTTCCTTGCGGATCGGCTCACGGTGTGATAATTGTCTACGCCGCGACCGTTGAAGCGTTTTAATGGGCCAGCTTCTAATCGTCTCTTGCGAGACAACATTCATCGAACTCTGACCTCAAATCAGGTAGGACTACCCGCTGAACTT"
resultado = analisar_sequencia(sequencia)
exibir_resultados(resultado)