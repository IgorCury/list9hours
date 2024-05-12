import random

usuario = 0
pc = 0

opcoes = ['pedra', 'papel', 'tesoura']

while True:
    user = input('Escolha: Pedra/Papel/Tesoura ou s para sair:' + ' ').lower()
    if user == 's':
        break

    if user not in opcoes:
        continue    

    roda_num = random.randint(0, 2)
    pc_pick = opcoes[roda_num]
    print('Computador escolheu:', pc_pick + '.')

    if user == 'pedra' and pc_pick == 'tesoura':
        print('Você venceu!')
        usuario += 1
    elif user == 'papel' and pc_pick == 'pedra':
        print('Você venceu!')
        usuario += 1
    elif user == 'tesoura' and pc_pick == 'papel':
        print('Você venceu!')
        usuario += 1
    else:
        print("Você perdeu, turururu")   
        pc += 1 

print('Você venceu', usuario, 'vezes.')
print('O computador venceu', pc, 'vezes.')
print('Até mais!')
