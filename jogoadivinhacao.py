from random import randint

seu_nome = input('Qual seu nome? ')
print(
    f'Ok! {seu_nome}, Eu estou escolhendo um número de 1 até 10. Você consegue adivinhar. '
)
numero_adivinhado = randint(1, 10)
numero_tentativas = 3

for tentativa in range(1, numero_tentativas + 1):
    numero_escolhido = int(input('Escolha um numero: '))
    if numero_escolhido == numero_adivinhado:
        print(f'Parabens, você acertou em {tentativa} tentativas!')
        break
    elif numero_escolhido > numero_adivinhado:
        print('Escolha um numero menor!')
    else:
        print('Escolha um numero maior!')

if numero_escolhido != numero_adivinhado:
    print(f'O número era {numero_adivinhado}. Obrigado por jogar!')