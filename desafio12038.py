n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
if n1 > n2:
    print('\033[35mO primeiro número é maior.\033[m')
elif n1 < n2:
    print('\033[7mO segundo número é maior.\033[m')
elif n1 == n2:
    print('\033[34mOs dois valores são iguais.\033[m')
