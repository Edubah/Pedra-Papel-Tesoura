# Neste projeto o foco é trabalhar com random.choice(), instruções if, além de obter entradas do usuário

import random

def play():
    user = input('O que você escolhe? ''R para pedra, P para papel ou S para tesoura\n')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'É um \'Empate!'

    #R > S, S > P, P > R
    if se_ganhar(user, computer):
        return 'Você ganhou!!!'
    return 'Você perdeu...'

def se_ganhar(player, oponente):
    #Retorna em VERDADE se o player ganhar
    # R > S, S > P, P > R
    if(player == 'r' and oponente == 's') or (player == 's' and oponente == 'p') \
        or (player == 'p' and oponente == 'r'):
        return True

print(play())