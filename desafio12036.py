casa = float(input('Qual o valor da casa que deseja financiar: R$'))
salário = float(input('Qual o valor do seu salário: R$'))
anos = int(input('Em quantos anos o senhor pretende pagar: '))
prestação = casa / (12 * anos)
if prestação > 0.3 * salário:
    print(f'\033[1;31mPerdão, mas seu empestimo foi negado!\033[m')
    print(f'\033[1;33mTente uma casa com um valor menor ou aumente a quantidade de anos do financiamento.\033[m')
else:
    print(f'\033[1;32mSeu financiamento foi aprovado.'
          f' O valor das parcelas será de R${prestação:.2f} durante {anos} anos.\033[m')
