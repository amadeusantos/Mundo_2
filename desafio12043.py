peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('\033[1mVocê está abaixo do peso recomendado! Procure um médico para verificar sua saúde.\033[m')
elif imc <= 25:
    print('\033[32mParabéns! Você está com o peso ideal.\033[m')
elif imc <= 30:
    print('\033[33mVocê está com sobrepeso! procure fazer exercícios físicos diariamente.\033[m')
elif imc <= 40:
    print('\033[31mVocê está com obesidade! Procure mudar seu abitos alimentares com ajuda de um médico.\033[m')
elif imc > 40:
    print('\033[7;31mVocê está com obesidade mórbida! Procure um médico o mais breve possível.\033[m')
