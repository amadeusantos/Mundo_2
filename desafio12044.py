print(f'\033[1;37m{"Lojas Lutz":=^40}\033[m')
produto = float(input('Digite o valor do produto: R$'))
print("""Qual a forma de pagamento:
\033[32m[ 1 ] Á vista dinheiro/cheque;
\033[34m[ 2 ] Á vista no cartão;
\033[35m[ 3 ] 2x no cartão;
\033[31m[ 4 ] 3x ou mais no cartão.\033[m""")
forma = int(input('Digite o número relacionado: '))
if forma == 1 or forma == 2:
    valor = .9 * produto if forma == 1 else 0.95 * produto
    print(f'O produto sai R${produto:.2f} por R${valor:.2f}.')
elif forma == 3 or forma == 4:
    parcelas = 2 if forma == 3 else int(input('\033[1mQuantas parcelas deseja: \033[m'))
    valor = produto if forma == 3 else 1.20 * produto
    print(f'O produto sai por R${valor:.2f}, dividido em {parcelas}x de R${valor/ parcelas:.2f}.')
else:
    print('\033[7;31mOpção inválida! Tente novamente.\033[m')
