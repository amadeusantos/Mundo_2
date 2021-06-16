n = int(input('Digite um número inteiro: '))
print('\033[1mQual base de conversão deseja:\033[m')
print('\033[34mBinário = 1\033[m')
print('\033[35mOctal = 2\033[m')
print('\033[1;32mHexadecimal = 3\033[m')
bsc = int(input('Digite o valor da base desejada: '))
if bsc == 1:
    conversão = bin(n)
    print(f'O valor de {n} em Binário é {conversão[2:]}.')
elif bsc == 2:
    conversão = oct(n)
    print(f'O valor de {n} em Octal é {conversão[2:]}.')
elif bsc == 3:
    conversão = hex(n)
    print(f'O valor de {n} em Hexadecimal é {conversão[2:]}.')
else:
    print('\033[31mOpção inválida! Tente novamente.')
