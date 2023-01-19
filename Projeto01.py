
# Escudo, Espada, Cavalo e Arco e flecha

# Escudo proteção

# Espada ataque

# Cavalo fuga

# Arco e flecha



print('RPG DA SORTE')



from random import choice

#Opção do Computador em Lista
escolha_pc = ['Escudo', 'Espada', 'Cavalo', 'Arco e flecha']

#Escolha do Computador
escolha_pc_choice = choice(escolha_pc)


loop = True

while loop:
    #Opção do Computador em Lista
    escolha_pc = ['Escudo', 'Espada', 'Cavalo', 'Arco e flecha']

    #Escolha do Computador
    escolha_pc_choice = choice(escolha_pc)
    print('Eu já escolhi, agora é a sua vez')

    print("""
    Aviso:
    Escolha sabiamente, você só terá uma chance!
    """)

    print("""
    MENU DE OPÇÃO:
    [1] - Escudo
    [2] - Espada
    [3] - Cavalo
    [4] - Arco e flecha
    [5] - Sair do Jogo
    """)

    escolha_player = str(input('Minha vida depende disso, escolha sabiamente: '))

    #Escolha Player - Escudo
    if escolha_player == '1':
        if escolha_pc_choice == 'Escudo':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Não dá pra lutar assim!')
            print('EMPATE!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Espada':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Você se defendeu bem, continue assim!')
            print('INIMIGO VENCEU!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Cavalo':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Você está em desvantagem, mais sorte da próxima vez! ')
            print('INIMIGO VENCEU!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Arco e flecha':
            print('ESCOLHA Do COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: A flecha acertou o seu escudo, parabéns está vivo!')
            print('VOCÊ VENCEU!')
            print('|\/|' * 17)
    #Escolha Player - Espada
    elif escolha_player == '2':
        if escolha_pc_choice == 'Escudo':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Você atacou bem, continua assim!')
            print('VOCÊ VENCEU!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Espada':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Os dois morreram, tente de novo')
            print('EMPATE!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Cavalo':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Inimigo2'
                  ' está morto, porém, o cavalo permanece vivo!')
            print('VOCÊ VENCEU!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Arco e flecha':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESSULTADO: Agora você tem uma flecha na cabeça!')
            print('INIMIGO VENCEU!')
            print('|\/|' * 17)
    #Escolha Player - Cavalo
    elif escolha_player == '3':
        if escolha_pc_choice == 'Escudo':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Seu inimigo está em desvantagem, avante cavaleiro!')
            print('VOCÊ VENCEU!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Espada':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Você está morto, porém, seu cavalo permanece vivo!')
            print('INIMIGO VENCEU!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Cavalo':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RERSULTADO: Passeio a cavalo? Amo!')
            print('EMPATE!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Arco e flecha':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Você recebeu uma flecha, mais sorte da próxima vez!')
            print('INIMIGO VENCEU!')
            print('|\/|' * 17)
    #Escolha Player - Arco e flecha
    elif escolha_player == '4':
        if escolha_pc_choice == 'Escudo':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Você acertou o escudo do seu adversário')
            print('INIMIGO VENCEU!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Espada':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Agora o seu adversário tem uma flecha na cabeça!')
            print('VOCÊ VENCEU!')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Cavalo':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Bem na cabeça, ótima mira!')
            print('VOCÊ VENCEU')
            print('|\/|' * 17)
        if escolha_pc_choice == 'Arco e flecha':
            print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
            print('|\/|' * 17)
            print('RESULTADO: Estão mortos!')
            print('EMPATE!')
            print('|\/|' * 17)
            #Encerra o jogo
    elif escolha_player == '5':
        print('|\/|' * 17)
        print('Até uma próxima partida!')
        print('|\/|' * 17)

        loop = False
    else:
        print('Atenção, escolha errada!.')