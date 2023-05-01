# Jogo da palavra secreta

import os

palavra = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    tentativa = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(tentativa) > 1:
        print('Digite apenas uma letra.')
        continue
                
    if tentativa in palavra:
        letras_acertadas += tentativa

    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
             palavra_formada += '*'

    print('palavra: ', palavra_formada)

    if palavra_formada == palavra:
         os.system('cls')
         print('Voce ganhou!')
         print('A palavra era:', palavra)
         print('tentativas:', numero_tentativas)
         letras_acertadas = ''
         numero_tentativas = 0

    elif numero_tentativas > len(palavra) + 3:
            print('Voce tentou demais!')
            
            break
