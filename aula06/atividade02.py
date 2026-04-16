resposta = 'S'
while resposta != 'N':
    venda = float(input('Digite o valor da venda: '))
    if venda > 1000.00:
        desconto = venda * 0.1
        valor_total = venda - desconto
        print(f'El valor da venda com o desconto de: {desconto:.2f} é : {valor_total:.2f}')
    else:
        print(f'O valor da venda é: {venda}')
    
    resposta = input('Quer continuar? [S/N]: ').upper().strip()[0]
print('Programa encerrado.')
