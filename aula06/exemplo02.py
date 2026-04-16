## ESTRUTURA DE REPETIÇÃO WHILE

## Exemplo 1 - Números até 10
i = 1
while i <= 10:
    print(i)
    i += 1 #i = i + 1
    
# Exemplo 2
n = 1
soma = 0
while n != 0:
    n = int(input('Digite um número: '))
    soma += n
print(f'A soma total é: {soma}')

# Exemplo 3
resposta = 'S'
soma = 0
while resposta != 'N':
    numero = float(input('Digite o número: '))
    soma += numero
    resposta = input('Quer continuar? [S/N]: ').upper().strip()[0]

print(f'A soma total é: {soma}')