def pa():
    # Solicita ao usuário o primeiro termo, o número de termos e a razão da PA
    a1 = int(input("Primeiro termo: "))
    n = int(input("Número de termos: "))
    r = int(input("Razão: "))
    
    # Calcula o valor do n-ésimo termo da PA
    an = a1 + (n - 1) * r
    
    # Imprime o valor do n-ésimo termo
    print("Último termo:", an)

# Chama a função para calcular e imprimir o n-ésimo termo da PA
pa()
