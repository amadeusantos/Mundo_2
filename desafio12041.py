from datetime import date

nasci = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasci
if idade <= 9:
    print('Você é um nadador: \033[4;33mMirim\033[m.')
elif idade <= 14:
    print('Você é um nadador: \033[32mInfantil\033[m.')
elif idade <= 19:
    print('Você é um nadador: \033[1;37mJunior\033[m.')
elif idade <= 25:
    print('Você é um nadador: \033[1;35mSênior\033[m.')
else:
    print('Você é um nadador: \033[1;31mMaster\033[m.')
