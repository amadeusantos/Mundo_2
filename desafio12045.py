from random import choice
from time import sleep

mãos = ['pedra', 'papel', 'tesoura']
pc = choice(mãos)
print('Vamos brincar de Pedra, Papel e Tesoura:')
pessoa = str(input('Escolha sua mão: ')).strip().lower()
print('\033[1;37mJo')
sleep(1)
print('\033[1;34mQuem')
sleep(1)
print('\033[31mPô\033[m')
sleep(1)
if pessoa in mãos:
    if pc == pessoa:
        print(f'\033[33mDeu empate! nôs dois jogamos {pc}.\033[m')
    elif pc == 'pedra' and pessoa == 'tesoura' or pc == 'papel' and pessoa == 'pedra' or \
            pc == 'tesoura' and pessoa == 'papel':
        print(f'\033[34mEu ganhei! Eu coloquei {pc} e você {pessoa}.')
    else:
        print(f'\033[35mParabéns você venceu!!! Você colocou {pessoa} e eu {pc}.')
else:
    print('\033[31mVocê digitou algo inválido! Tente novamente.\033[m')
