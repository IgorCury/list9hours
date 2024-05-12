#importa o random
import random

'''
# gera um numero aleatorio
r = random.randint(-5, 11)
print(r)
'''

num = input("Escolha um numero!")
if num.isdigit():
    num = int(num)

    if num <= 0:
        print('Por favor, escolha um numero maior que 0')
        quit()

else:
   print('Por favor, escolha um numero maior que 0')
   quit()

rand = random.randint(0, num)
print(rand)
tentativas = 0
while True:   
    tentativas += 1
    user = input("Qual você acha que é: ")
    if user.isdigit():
       user = int(user)
    else:
        print('Por favor, escolha um numero maior que 0')
        continue
    
    if user == rand:
        print("Você acertou")  
        break 

    else:
        if user > rand:
            print('Você está acima!')
        else:
            print("Você está abaixo!")

print('Isso! você precisou de', tentativas)