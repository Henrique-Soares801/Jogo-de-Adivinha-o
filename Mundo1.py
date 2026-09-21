from random import randint
from time import sleep

computador = randint(0, 5)

palpite = int(input(' Adivinhe o Número de 0 a 5 '))


print('Pensando...')
sleep(3)


if palpite == computador:
    print('Você Acertou')
else:
    print(f' Você errou! O número era {computador}')