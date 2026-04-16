#### Calcula a media de um aluno
# n1 = float(input('Nota 1: '))
# n2 = float(input('Nota 2: '))
# media = (n1 + n2) / 2

##ESTRUTURA DE REPETIÇÃO (for)
# for num in range(5):
#     print('Hi!')

# for i in range(10,21):
#     print(i)

# qtde = int(input('Quer contar até quanto? '))    
# for i in range(qtde):
#      print(i, end=' ') #Imprime na mesma linha.

#soma = 0
# for u in range(3):
#     print(f'\nRodada {u + 1}')
#     num1 = int(input('Informe o primer número: '))
#     num2 = int(input('Informe o segundo número: '))
#     soma = num1 + num2
#     print(f'O total é {soma}')

### Variável Acumuladora
# soma = 0
# for i in range(5):
#     numero = float(input('Digite um número: '))
#     #soma = soma + numero
#     soma += numero

# print(f'A soma dos números digitados é: {soma}')

# soma = 0
# for v in range(5):
#     venda = float(input('Informe o valor: '))
#     if venda > 100 :
#         soma += venda
#         print(f'Valor R$ {venda} somada.')
#         print(f'A soma parcial é {soma}')
#     else:
#         print('Valor não computado.')
# print(f'\nA soma total é {soma}')
m = int(input('Digite a quantidade de alunos: '))
p = int(input('Digite a quantidade de avaliações: '))
print('----------------------------------------')
for aluno in range(m):
    print(f'Digite as quatro notas do aluno {aluno + 1}')
    soma = 0
    for nota in range(p):
        nota = float(input(f'Digite a nota {nota +1} do aluno {aluno + 1}: '))
        soma += nota
    media = soma / p
    print(f'A media do aluno {aluno + 1} é {media:.2f}')
    if media >= 6:
        print('Aprovado')
    else: 
        print('Reprovado')
    print('')   
