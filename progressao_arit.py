# Solicita o primeiro termo da sequência e a razão ao usuário
p = float(input('Digite o primeiro termo: '))
r = float(input('Digite a razão: '))

# Inicializa a variável a como o primeiro termo
a = p

# Imprime o primeiro termo
print(p)

# Loop para calcular e imprimir os próximos 9 termos da sequência
for c in range(0, 9):
    a = a + r  # Calcula o próximo termo somando a razão ao termo atual
    print(a)  # Imprime o próximo termo

# O valor de a é inicializado com o valor de p, que é o primeiro termo da sequência. 
# Isso é feito apenas para garantir que o primeiro termo seja incluído na impressão 
# da sequência.