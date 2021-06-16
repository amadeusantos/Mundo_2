nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
if média < 5:
    print(f'\033[31mREPROVADO!!! Sua média foi {média:.2f}.\033[m')
elif 5 <= média < 7:
    print(f'\033[1;33mVocê ficou de recuperação, pois sua média foi {média:.2f}.\033[m')
elif média >= 7:
    print(f'\033[32mVocê foi APROVAODO!!! Parabéns, sua média foi {média:.2f}.\033[m')
