name = input('Como você gostaria de ser chamado?'' ')
print('Bem vindo ao mundo magico de TimeAdvent', name,'Sua aventura começa agora!')

resposta = input(
    'Role os dados e diga se deseja ir para esquerda ou direita:' + '').lower()

if resposta == 'esquerda':
    resposta = input('Você precisa atravessar o rio, tentar achar um lugar raso e passar andando ou ir por aqui nadando! digite nadar ou andar:'+' ')
    if resposta == 'nadar':
        print('Você tentou passar nadando e foi devorado por um jacaré!')
    elif resposta == 'andar':
        print('Você andou por milhas e milhas, acabou sua comida e agua, tentou beber a propria urina mas nao resolveu, você morreu!')
    else:
        print('Resposta incorreta!') 

elif resposta == 'direita':
        resposta = input('Você avistou uma ponte mas ficou com medo de atravessar vai tentar passar ou vai voltar?:'+' ')
        
        if resposta == 'voltar':
            print('Você voltou para o inicio e perdeu tudo, comece novamente!')
        elif resposta == 'atravessar':            
            resposta = input('Você encontrou um estranho que começou a conversar deseja ouvir o que ele tem para falar?(sim/não)')
            
            if resposta == 'sim':
                 print('Ele é o dono do mundo AdventTim, ele te ouro e você venceu')
            elif resposta == 'nao':
                 print('Ele é o dono do mundo AdventTim, ele ficou furioso com seu desdem e transformou em uma galinha!')
            else:
                print('Resposta incorreta! Você morreu!') 

        else:
            print('Resposta incorreta! Você morreu!') 
else:
    print('Resposta incorreta!') 

print('Obrigado por participar!')


