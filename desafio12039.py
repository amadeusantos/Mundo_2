import datetime

nasci = int(input('Qual seu ano de nacimento: '))
ano = datetime.date.today().year
idade = ano - nasci
if idade < 18:
    print(f'\033[32mTudo certo! Seu alistamento será daqui {nasci + 18 - ano} anos.\033[m')
elif idade == 18:
    print('\033[33mVocê deve se apresentar o mais breve possivel a uma junta militar!\033[m')
elif idade > 18:
    print(f'\033[31mSeu alistamento foi a {ano - (nasci + 18)} anos! '
          'Caso ainda não tenha se apresentado ao serviço militar, '
          'o senhor está sujeito a perder direito previstos na constituição.\033[m')
