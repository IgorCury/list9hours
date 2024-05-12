print("Bem vindo ao meu jogo")

jogo = input("Vamos jogar?")


if jogo.lower() != "sim":
    quit()      
print("Oba, bora lá")
score = 0

responda = input('Qual a sigla de Central de processamento?')
if responda.lower()  == 'cpu':
    print('PERFEITO!')
    score += 1
else:
    print("Tá errado!")

responda = input('Para que serve uma GPU?')
if responda.lower()  == 'grafico de processamento':
    print('PERFEITO!')
    score += 1
else:
    print("Tá errado!")

responda = input('Para que serve a RAM?')
if responda.lower()  == 'acesso aletorio de memoria':
    print('PERFEITO!')
    score += 1
else:
    print("Tá errado!")

responda = input('Para que serve PSU')
if responda.lower()  == 'fonte de energia':
    print('PERFEITO!')
    score += 1
else:
    print("Tá errado!")

print('Você é o cara! Você fez' ' ' +  str(score) + ' ' 'acertos')


