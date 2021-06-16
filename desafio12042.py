l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    if l1 == l2 == l3:
        print(f'Os segmentos {l1}, {l2} e {l3} formam um triângulo \033[34mequilátero\033[m.')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print(f'Os segmentos {l1}, {l2} e {l3} formam um triângulo \033[35mescaleno\033[m.')
    else:
        print(f'Os segmentos {l1}, {l2} e {l3} formam um triângulo \033[32misósceles\033[m.')
    # triângulo = 'equilátero' or 'escaleno' or 'isósceles'
    # print(f'Os segmentos {l1}, {l2} e {l3} formam um triângulo {triângulo}.')
else:
    print(f'Os segmentos {l1}, {l2} e {l3} \033[31mNão formam um triângulo\033[m.')
