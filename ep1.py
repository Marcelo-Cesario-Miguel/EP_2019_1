# EP 2019-1: Escape Insper
#
# Alunos:
# - aluno A: Marcelo Miguel, marcelocm8@al.insper.edu.br
# - aluno B: Byron Hans, byronhboe@al.insper.edu.br


#definição de todos os cenários

# Python program to print 
  

 
cenário = {
        "Prédio 1":"Você está em frente ao prédio 1, o que deseja fazer?",
        "Elevador":"Você está no elevador, selecione um andar:",
        "Saguão":"Você está no saguão do prédio 1, o que deseja fazer?", 
        "Biblioteca":"Você está na biblioteca do olhar penetrante",
        "Prédio 2":"Você está infiltrado no prédio 2, o covil do Raul",
        "Humberto":"Você está infiltrado na sala do Humberto",
        "Raul":"Você está infiltrado na sala do Raul. Se prepare Jogador, se chegou até aqui, terá que ir até o final"}



#início do código do jogo
inventário = []
from colorama import Fore, Style 
import time
vida = 100 #vida do jogador
vida_boss = 1000 #vida do veterano (primeiro chefão)
i = 0 #contador para linha do título
jogo = True #o jogo funciona enquanto for true 
derrota = "GAME OVER! x__x " 
Vitória = "Parabéns! Você venceu! Agora vá fazer o EP1!¯\_(ツ)_/¯"

while jogo == True:
    print(Fore.BLUE + "KITARA: Olá Insperiano, meu nome é Kitara, sou um espectro"
      " invisível vindo de outra de dimensão. Fui enviada porque você"
      " precisa conseguir adiar a entrega do EP1 de Design de Software"
      " senão você e todos os seus colegas vão pegar DP nessa matéria!!!"
      " Ficarei com você até conseguir, só então poderei voltar para minha"
      " dimensão!")
    print(Style.RESET_ALL) 
    time.sleep(1)
    
    print("")
    
    print(cenário["Prédio 1"])
    i = len(cenário["Prédio 1"])
    print(i*"-")
    time.sleep(2)
    
    opção_1 = "A: Sair correndo com medo da Kitara."
    opção_2 = "B: Pedir para Kitara explicar melhor quem ela é."
    
    print("")
    
    print(opção_1)
    time.sleep(1)
    print(opção_2)
    time.sleep(2)
    
    escolha = input("Digite aqui a opção que deseja: ")
    
    print("")
    
    while escolha != "A" and escolha != "B":
        time.sleep(2)
        print("Opção inválida, digite A ou B.")
        escolha = input("Digite aqui a opção que deseja: ")
        
    if escolha == "A":
        time.sleep(2)
        print("Essa não, você correu para rua e morreu atropelado!")
        jogo = False
    elif jogo == False:
        time.sleep(2)
        print(derrota)
        break
        
    elif escolha == "B":
        time.sleep(2)
        print("")
        print("VOCÊ: Que diabos está acontecendo e como assim você é um"
           " espectro invisível de outra dimensão?! Eu tô ficando maluco?!")
        
        print("")
        time.sleep(2)
        
        print(Fore.BLUE + "KITARA: Não há tempo para explicações Insperiano! Você precisa"
          " adiar o EP1 para o bem de todos! Aliás, qual o seu nome?")
        time.sleep(2)
        print(Style.RESET_ALL) 
        nome_do_jogador = input("Digite seu nome: ")
        print("")
        time.sleep(2)
        
        print(Fore.BLUE + "KITARA: Certo {},"
      " precisamos encontrar seu professor!".format(nome_do_jogador))
        print(Style.RESET_ALL) 
        print("")
        time.sleep(2)
    
        print(cenário["Prédio 1"])
        i = len(cenário["Prédio 1"])
        print(i*"-")
        time.sleep(2)
        
        opção_1 = "A: Ir para o prédio 2."
        opção_2 = "B: Ir para o saguão do prédio 1."
        
        print(opção_1)
        time.sleep(1)
        print(opção_2)
        time.sleep(1)
        
        escolha = input("Digite aqui a opção que deseja: ")
        print("")
        while escolha != "A": #obrigar o jogador a passsar por A controle de input
            if escolha == "B":
                time.sleep(2)
                print('')
                print("VOCÊ: O Raul deve estar no prédio 2, acho melhor ir"
                      " para lá...")
                time.sleep(2)
                print('')
                escolha = input("Digite aqui a opção que deseja: ")
            else:
                print("Opção inválida, digite A ou B.")
                time.sleep(2)
                print("")
                escolha = input("Digite aqui a opção que deseja: ")
                print('')
        
                                
        if escolha == "A":
            time.sleep(2)
            print('')
            print("Ao tentar atravessar a rua para ir ao prédio 2, uma força"
                  " magnética te joga com tudo para trás!"
                  " As pessoas ao redor de te olham feio brevemente e tornam"
                  " a seguir seus caminhos novamente.")
            print("")
            time.sleep(2)
            print(Fore.BLUE + "KITARA: Essa não, forças inimigas interdimensionais estão"
                  " tentando nos impedir! Você não vai conseguir acessar"
                  " o prédio 2 por enquanto! Vamos para o saguão!")
            print(Style.RESET_ALL)
            print("")
            time.sleep(2)
            print("VOCÊ: Isso tudo é uma loucura Eu só posso estar sonhando,"
                  " mas vamos lá!")
            print("")
            time.sleep(3)
        
        print(cenário["Saguão"])
        i = len(cenário["Saguão"])
        print(i*"-")
        print('')
        
        
        opção_1 = "A: ir para a biblioteca."
        time.sleep(1)
        opção_2 = "B: ir para o elevador."
        
        
        print(opção_1)
        time.sleep(2)
        print(opção_2)
        time.sleep(2)
        
        
        escolha = input("Digite aqui opção que deseja: ")
        time.sleep(2)
        
        while escolha != "A" and escolha != "B": 
            time.sleep(2)
            print("Opção inválida, digite A ou B.")
            time.sleep(2)
            print("")
            escolha = input("Digite aqui a opção que deseja: ")
            time.sleep(2)
            
        
        if escolha == "B":  
            print("")
            print("Você tenta acessar os eladores mas novamente uma força"
                  "magnética te joga para trás com tudo!")
            print('')
            time.sleep(2)
            print("VOCÊ: denovo isso! Ai que dor!")
            time.sleep(2)
            print('')
            print("As pessoas te encaram brvevemte e não esboçam nenhuma outra"
                  " reação apesar do que aconteceu")
            time.sleep(2)
            print('')
            print("VOCÊ: Kitara, por que ninguém está reagindo a tudo isso?"
                  " Eu estou invisível também?")
            time.sleep(2)
            print('')
            print(Fore.BLUE + "KITARA: Não, não está, repare que muitas delas te encaram,"
                  " pelas energias que eu estou sentindo, elas estão possuidas"
                  " pelas mesmas forças malignas interdimensionais que criam"
                  " os campos magnéticos que te impedem de entrar em"
                  " determinados lugares.")
            time.sleep(2)
            print(Style.RESET_ALL)
            print('')
            print("VOCÊ: pera aí, você consegue sentir os campos magnéticos e"
                  " as energias malignas?")
            time.sleep(2)
            print('')
            print(Fore.BLUE + "KITARA: Sim hahaha, desculpe não te avisar, é que...")
            time.sleep(1)
            print(Style.RESET_ALL)
            print('')
            print("VOCÊ: Nossa mano, se eu te enxergasse te deitava na" 
                  " porrada!")
            print('')
            time.sleep(2)
            print(Fore.BLUE + "KITARA: HAHAHAH, sem mais delongas, vamos para a" 
                  " biblioteca! Parece um lugar menos perigoso...")
            print(Style.RESET_ALL)
            print('')
            time.sleep(2)
        
        print('')
        print(cenário["Biblioteca"])
        i = len(cenário["Biblioteca"])
        print(i*"-")
        time.sleep(2)
        print('')
        print("Você está na entrada da biblioteca e novamente as pessoas"
              " te olham feio brevemente antes de retomar o que faziam.")
        print('')
        time.sleep(2)
        print("Você percebe que tem um veterano que continua te encarando.")
        print('')
        time.sleep(2)
        
        opção_1 = "A: encarar de volta com a testa franzida."
        opção_2 = "B: desviar o olhar."
        
        print(opção_1)
        time.sleep(1)
        print(opção_2)
        time.sleep(1)
        
        escolha = input("Digite aqui o deseja fazer: ")
        
        while escolha != "A" and escolha != "B": #das duas formas o veterano ataca
            time.sleep(2)
            print("Opção inválida, digite A ou B.")
            time.sleep(2)
            print("")
            escolha = input("Digite aqui a opção que deseja: ")
            time.sleep(2)
            print("")
        
        if escolha == "A":
            print('')
            print(Fore.BLUE + "KITARA: Ele é esta possuido," 
                   " cuidado {}!".format(nome_do_jogador))
            print(Style.RESET_ALL)
        
        print('')    
        print("O veterano começa a andar na sua direção com um olhar mortal.")
        time.sleep(2)
        print('')    
        print(Fore.BLUE + "KITARA: essa não! Ele vai está possuido e vai nos atacar!")
        print(Style.RESET_ALL)
        opção_1 = "A: Correr. "
        opção_2 = "B: Encará-lo com um olhar firme"
        
        print(opção_1)
        time.sleep(1)
        print(opção_2)
        time.sleep(1)
        print('')
        
        escolha = input("Digite aqui a opção que deseja: ")
        
        
        while escolha != "A" and escolha != "B":
            time.sleep(2)
            print("Opção inválida, digite A ou B.")
            time.sleep(2)
            print("")
            escolha = input("Digite aqui a opção que deseja: ")
            time.sleep(2)
            print("")
        
        
        if escolha == "A":
            print('')
            print(Fore.BLUE + "KITARA: Nãooo! Não corra, ele se você correr você morre!")
            print(Style.RESET_ALL)
            print('')
            time.sleep(2)
            print("O veterano te alcançou, entrou dentro do seu corpo,"
                  " consumiu sua alma e você caiu duro, como se fosse um"
                  " infarto fulminante.")
            print('')
            jogo = False
        
        elif jogo == False:
            print(derrota)
            break
        
        else:
            print(" O veterano  olhou bem no fundo dos seus olhos e te levou"
                  " para uma outra dimensão. Vocês estão num campo de"
                  " batalha!")
            print('')
            time.sleep(2)
            print("VOCÊ: Meu Deus! Onde eu estou?! Como eu vim parar aqui?!")
            print('')
            time.sleep(2)
            print(Fore.BLUE + "KITARA: Essa não, o veterano possuido de te invocou para"
                  " uma dimensão de guerra! Você terá que lutar com ele!")
            print(Style.RESET_ALL)
            print('')
            time.sleep(2)
            print("VOCÊ: Como assim eu vou ter que lutar?!")
            print('')
            time.sleep(2)
            print(Fore.BLUE + "KITARA: Você faz muitas perguntas! Controle o medo!"
                  " Preste bem atenção você tem 100 pontos de vida"
                  " se você perder esses 100 pontos, vc morre e estará tudo"
                  " acabado! Não deixei o seu inimigo te acertar!"
                  " Nessa dimensão eu tenho o poder de forjar um único"
                  " equipamento para você lutar!")
            print(Style.RESET_ALL)
            opção_1  = "A: Espada divina - Causa 700 de dano"
            opção_2  = "B: Escudo divino - Reflete até 500 de dano"
            
            print(opção_1)
            time.sleep(1)
            print(opção_2)
            time.sleep(1)
            print('')
            
            
            escolha  = input("Digite aqui a opção que deseja: ")
            
            
            while escolha != "A" and escolha != "B": #das duas formas o veterano ataca
                time.sleep(2)
                print("Opção inválida, digite A ou B.")
                time.sleep(2)
                print("")
                escolha = input("Digite aqui a opção que deseja: ")
                time.sleep(2)
                print("")
            
            print('')
            print(Fore.BLUE + "KITARA: agora que você escolheu seu equipamento,"
                   "lute como um bravo guerreiro!")
            print(Style.RESET_ALL)
            time.sleep(2)
            print('')
            print("VOCÊ: Meu Deus do céu Berg, que coisa maluca mas"
                  " vamos lá, por Demaciaa!!!")
            print('')
            time.sleep(2)
            
            if escolha == "A":
                print("Prepare-se para o combate!")
                time.sleep(2)
                print('')
                print("{} VERSUS O Veterano Sugador" 
                      " de Almas".format(nome_do_jogador))
                time.sleep(2)
                print('')
                print("HP - {}: ".format(nome_do_jogador))
                print(vida)
                print('')
                print("HP - O Veterando Sugador de Almas: ")
                print(vida_boss)
                print('')
                print('')
                time.sleep(3)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print('')
                print("FIGHT")
                print('')
                time.sleep(2)
                print("***CLAAASH***")
                print('')
                vida -= 525
                vida_boss -= 700
                print("Dano recebido: 525")
                time.sleep(1.5)
                print("Dano causado: 700")
                time.sleep(1.5)
                print('')
                print("HP - {}: ".format(nome_do_jogador))
                print(vida)
                time.sleep(1.5)
                print('')
                print("HP - O Veterando Sugador de Almas: ")
                print(vida_boss)
                time.sleep(1.5)
                print('')   
                jogo = False
            
            elif jogo == False:
                print(derrota)
                break
            
            if escolha == "B":
                print("Prepare-se para o combate!")
                time.sleep(2)
                print('')
                print("{} VERSUS O Veterano Sugador" 
                      " de Almas".format(nome_do_jogador))
                time.sleep(2)
                print('')
                print("HP - {}: ".format(nome_do_jogador))
                print(vida)
                print('')
                print("HP - O Veterando Sugador de Almas: ")
                print(vida_boss)
                print('')
                print('')
                time.sleep(3)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print('')
                print("FIGHT")
                print('')
                time.sleep(2)
                print("***CLAAASH***")
                print('')
                vida -= 25
                vida_boss -= 500
                print("Dano recebido: 25")
                print("Dano causado: 500")
                print('')
                print("HP - {}: ".format(nome_do_jogador))
                print(vida)
                print('')
                print("HP - O Veterando Sugador de Almas: ")
                print(vida_boss)
                print('')    
                
                #segundo ataque
                
                time.sleep(2)
                print('')
                print("HP - {}: ".format(nome_do_jogador))
                print(vida)
                print('')
                print("HP - O Veterando Sugador de Almas: ")
                print(vida_boss)
                print('')
                print('')
                time.sleep(3)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print('')
                print("FIGHT")
                print('')
                time.sleep(2)
                print("***CLAAASH***")
                print('')
                vida -= 25
                vida_boss -= 500
                print("Dano recebido: 25")
                print("Dano causado: 500")
                print('')
                print("HP - {}: ".format(nome_do_jogador))
                print(vida)
                print('')
                print("HP - O Veterando Sugador de Almas: ")
                print(vida_boss)
                print('')
                time.sleep(1)
                
            print(Fore.RED + "YOU WIN")
            print('')
            time.sleep(3)
            print(Style.RESET_ALL)
            print(Fore.BLUE + "KITARA: Sábia escolha campeão, lutou como um guerreiro."
                  " O Veterano deixou algo mágico, pegue para você!")
            print('')
            time.sleep(1)
            print(Style.RESET_ALL)
            inventário.append("Chave do elevador")
            inventário.append("Escudo divino")
            inventário.append("Instruções para derrubar o servidor de desafios")
            print(Fore.BLUE + "KITARA:Você pegou itens mágicos! Acesse seu inventário,"
                  " mais conhecido commo sua mochila, para ver o que pegou!")
            print('')
            time.sleep(2)
            
            print(Style.RESET_ALL)
            print(inventário)
            print('')
            time.sleep(2)
            print(Fore.BLUE + "KITARA: Parabéns, agora acredito que poderemos acessar o elevador,"
                  " vamos voltar para o saguão do Prédio 1")
            time.sleep(2)
            print(Style.RESET_ALL)
            print('')
            print("VOCÊ: Essas instruções, talvez elas possam servir como"
                  " moeda de troca para convencer o Raul a adiar o EP....")
            print('')
            time.sleep(2)
        
            print(cenário["Saguão"])
            i = len(cenário["Saguão"])
            print(i*"-")
            print('')
        
        
            opção_1 = "A: ir para a biblioteca."
            time.sleep(1)
            opção_2 = "B: ir para o elevador."
        
        
            print(opção_1)
            time.sleep(2)
            print(opção_2)
            time.sleep(2)
        
        
            escolha = input("Digite aqui opção que deseja: ")
            time.sleep(2)
        
            while escolha != "B":
                if escolha != "A":
                    print("Opção inválida, digite A ou B.")
                    time.sleep(2)
                    print("")
                    escolha = input("Digite aqui a opção que deseja: ")
                    
                if escolha == "A":
                    print("Você vê que o veterano que você lutou esta morto,"
                          " no meio da biblioteca,"
                          " porém ninguem parece se importar com isso")
                    print('')
                    time.sleep(2)
                    print("VOCÊ: Espera aí! Eu matei uma pessoa!"
                          " Eu vou ser preso!")
                    time.sleep(2)
                    print('')
                    print(Fore.BLUE + "KITARA: Calma {0}, ninguem vai ser preso,"
                          " ainda, se você vencer tudo isso"
                          " tudo voltará ao normal, inclusive o veterano morto."
                          " Agora precisamos ir para o elevador,"
                          " vamos lá {0}!".format(nome_do_jogador))
                    time.sleep(2)
                    print(Style.RESET_ALL)
                    print('')
                    time.sleep(2)
                    
                    
                    
            print(cenário["Elevador"])
            i = len(cenário["Elevador"])
            print(i*"-")
            print('')
            print("Voce percebe que no elevador, tem uma entrada para a chave que o Veterano dropou")
            time.sleep(2)
            print ("")
            print(Fore.BLUE + "KITARA: vamos colocar a chave, acredito que algo irá acontecer")
            time.sleep(1)
            print(Fore.MAGENTA + "Chave do elevador foi removida do seu inventario")
            print('')
            time.sleep(2)
            print(Style.RESET_ALL)
            inventário.remove("Chave do elevador")
            print(inventário)
            print('')
            time.sleep(2)
            print ("A chave absorve a energia magnética e explode"
                   ", O elevador liga e começa a tocar aquela famosa música de elevador...")
            print('')
            time.sleep(2)
            print ("Começa a fazer um barulho estranho, a velocidade do elevador começa a aumentar sem ninguem ter acionado nada")
            time.sleep(2)
            print('')
            print(Fore.BLUE + "KITARA: {0}, acredito que esse elevador não seja"
                  " um simples elevador, pela minha experiência,"
                  " acredito que ele seja algum tipo de portal".format(nome_do_jogador))
            print(Style.RESET_ALL)
            print("")
            time.sleep(2)
            print("VOCÊ: Um PORTAL?! Kitara eu so quero adiar o EP, então POR QUE DIABOS VOCÊ ME LEVOU PARA UM PORTAL?!")
            print ("")
            time.sleep(2)
            print(Fore.BLUE + "KITARA: {0}, isso é muito mais sério do que um simples EP, você não percebeu o que o Raul realmente deseja fazer? Vou te explicar: o Raul é o responsável por tudo isso.".format(nome_do_jogador))
            time.sleep(3)
            print('')
            print(Fore.BLUE + " KITARA: Depois que um aluno encontrou o Facebook dele, o mundo nunca mais foi o mesmo."
                  " o Raul ficou indignado com o acontecimento, e em meio a essa situação, ele recorreu a magias negras, junto com seu assistente Humberto.")
            time.sleep(4)
            print('')
            print(Fore.BLUE + "KITARA: Além disso, acredito que ele deva estar no Prédio 2. Vou tentar simplificar esse portal para a sua linguagem")
            print(Style.RESET_ALL)
            time.sleep(1)
            print('')
            print (" tente clicar no primeiro botão, acho que iremos para o elevador do Prédio 2")
            time.sleep(1)
            print(Style.RESET_ALL)
            print('')
            botão= input("Clicar no botão?(S/N)")
            
            
            
            while botão !="S":
                if botão != "N":
                    print(Fore.BLUE + "KITARA, vamos {0}, responda com S ou N".format(nome_do_jogador))
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    botão= input("Clicar no botão?")
                if botão == "N":
                    print(Fore.BLUE + "KITARA: {0}, me desculpe, mas o mundo depende da sua decisão, voce DEVE apertar o botão.".format(nome_do_jogador))
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    botão= input("Clicar no botão?")
                    
            print('')            
            print(Fore.BLUE + "KITARA: Muito bem, acho que esta funcionando, vamos para o Prédio 2!")
            print(Style.RESET_ALL)
#PREDIO 2
            print (cenário["Prédio 2"])
            i = len(cenário["Prédio 2"])
            print(i*"-")
            print('')
            time.sleep(2)
            print(Fore.BLUE + "KITARA: Parece que deu certo, estamos dentro do Prédio 2,"
                  " vamos procurara ele.")
            print(Style.RESET_ALL)
            print("Ao sair do elevador do Predio 2, Você se depara com duas salas, uma com com a placa escrito"
                  " Raul e a outra escrito Humberto.")
            time.sleep(1)
            sala=input ("Deseja ir para a sala da esquerda(Raul), ou para a da direita(Humberto)")  
            print('')
            while sala != "Raul" and sala !="Humberto":
                print ("Responda com Raul ou Humberto")
                sala=input ("Deseja ir para a sala da esquerda(Raul), ou para a da direita(Humberto)")
                print('')
            if sala == "Humberto":
                print('')
                print (cenário["Humberto"])
                i = len(cenário["Humberto"])
                print(i*"-")
                print('')
                time.sleep(2)
                print("Ao entrar na sala do Raul, Você se depara com o Humberto interrogando o aluno que descobriu o facebook do Raul")
                time.sleep(1)
                print('')
                print(Fore.BLUE + "KITARA: Meu deus {0}, que horrível, você deve intervir".format(nome_do_jogador))
                print(Style.RESET_ALL)
                print('')
                print ("A: Nocautear o Humberto com o Escudo")
                print ("B: Gritar com ele e tentar dar uma de durão")
                escolha_humberto=input ("ADigite aqui a opção que deseja: ")
                
                while escolha_humberto !="A" and escolha_humberto !="B":
                    print ("Opção invalida, por favor responda com A ou B")
                    escolha_humberto=input ("A ou B? Digite seu código aqui")
                if escolha_humberto =="B":
                    print ("Voce tentou gritar com o Humberto")
                    time.sleep(1)
                    print(Fore.RED + " Humberto olhou para você com um ódio mortal")
                    print ("seus olhos começaram a ficar VERMELHO")
                    time.sleep(1)
                    print ("Ele olhou dentro da tua alma")
                    print (".")
                    time.sleep(1)
                    print (".")
                    time.sleep(1)
                    print (".")
                    time.sleep(1)
                    print("E simplesmente, você morreu!")
                    print(Style.RESET_ALL)
                    jogo = False
            if jogo == False:
                time.sleep(2)
                print(derrota)
                break
                if escolha_humberto =="A":
                    print("Voce correu, por trás dele, tentou um nocaute e...")
                    time.sleep(2)
                    print('')
                    print("Seu escudo quebrou! e foi removido do seu inventário!")
                    print('')
                    inventário.remove("Escudo divino")
                    print(inventário)
                    print("Nocaute foi realizado com sucesso")
                    print("Humberto caí duro no chão")
                    time.sleep(2)
                    print('')
                    print(Fore.LIGHTBLUE_EX + "ALUNO: Obrigado {}, você me salvou, não sei o que aconteceria sem você!".format(nome_do_jogador))
                    print("Pensei que iria morrer, tome, o segredo não pode morrer comigo")
                    print(Fore.MAGENTA + "Facebook do Raul foi adicionado ao seu inventario") #easteregg
                    inventário.append("Facebook do Raul")
                    print('')
                    time.sleep
                    print(inventário)
                    print(Fore.BLUE + "KITARA: Muito bem {0}, agora acredito que estamos na vantagem, VAMOS ATRÁS DO RAUL!".format(nome_do_jogador))
                    print(Style.RESET_ALL)
                    time.sleep(2)
                    print('')
                print (cenário["Raul"])
                print (cenário["Raul"])
                i = len(cenário["Raul"])
                print(i*"-")
                print('')
                time.sleep(4)
                print(Fore.BLUE + "KITARA: Chegamos {0}, é aqui que a nossa jornada termina. Agora é por sua conta e risco, boa sorte jogador!".format(nome_do_jogador))
                print(Style.RESET_ALL)
                time.sleep(2)
                print ("VOCÊ: Agora é por minha conta, isso já está além de um simples EP, devo salvar minha faculdade!")
                print("*A sala parece estar vazia*")
                time.sleep(2)
                print ("VOCÊ: Raul, apareça. Ou irei atrás de você!")
                time.sleep(4)
                print("Logo após isso, o Raul aparece")
                print(Fore.RED + "Raul: Quem ameaça me perturbar?")
                print(Style.RESET_ALL)
                time.sleep(1)
                print("VOCÊ: O único que poderá te deter")
                print(Fore.RED + "Raul: Isso iremos ver")
                print(Fore.RED + "Raul: Humberto, apareça!")
                time.sleep(3)
                print(Fore.RED + "Raul: Humberto??")
                print(Style.RESET_ALL)
                print ("VOCÊ: Ta sentindo falta de alguém?")
                print ("VOCÊ: Agora o papo é o seguinte, ou você adia a entrega do EP, ou eu derrubo seu servidor"
                       " de desafios e divulgo sua conta do facebook!")
                print(Fore.RED + "Raul: Não creio, essas eram as duas coisas que eu considerava simplesmente impossível!"
                      " Você está blefando")
                print(Style.RESET_ALL)
                print('')
                print(Fore.MAGENTA +"Instruções para derrubaro servidor de desafios e Facebook do Raul foram removidos do seu inventário.")
                print(Style.RESET_ALL)
                time.sleep(1)
                print("Você mostra para o Raul seus dois trunfos...")
                time.sleep(1)
                inventário.remove("Facebok do Raul")
                inventário.remove("Instruções para derrubar o servidor de desafios")
                print(inventário)
                print(Fore.RED + "Raul: Não creio! Muito bem, feito. Mas lembre-se, se prepare para a PF, seu nome esta marcado!")
                print("Raul: Aliás, qual o teu nome? Acredito que devo saber quem me derrotou.")
                print(Style.RESET_ALL)
                time.sleep(1)
                print("VOCÊ: Meu nome? Meu nome é Noé, noé da sua conta!")
                time.sleep(2)
                print('')
                print(Fore.BLUE + "KITARA: Parabéns Insperiano, tudo voltará ao normal agora e eu retornei para minha dimensão!"
                      "Continue sempre brilhando assim, você é um verdadeiro herói!")
                print(Style.RESET_ALL)
                time.sleep(1)
                jogo == "Conseguiu!"
        if jogo == "Conseguiu!":
            time.sleep(2)
            print(Vitória)
            break
        if sala == "Raul":
            print (cenário["Raul"])
            print (cenário["Raul"])
            i = len(cenário["Raul"])
            print(i*"-")
            print('')
            time.sleep(4)
            print(Fore.BLUE + "KITARA: Chegamos {0}, é aqui que a nossa jornada termina. Agora é por sua conta e risco, boa sorte jogador!".format(nome_do_jogador))
            print(Style.RESET_ALL)
            time.sleep(2)
            print ("VOCÊ: Agora é por minha conta, isso já está além de um simples EP, devo salvar minha faculdade")
            print("*A sala parece estar vazia*")
            time.sleep(2)
            print ("VOCÊ: Raul, apareça. Ou irei atrás de você")
            time.sleep(4)
            print("Logo após isso, o Raul aparece")
            print(Fore.RED + "Raul: Quem ameaça me perturbar?")
            print(Style.RESET_ALL)
            time.sleep(2)
            print("VOCÊ: O único que poderá te deter")
            print(Fore.RED + "Raul: Isso iremos ver")
            time.sleep(2)
            print(Fore.RED + "Raul: Humberto, apareça!")
            print(Style.RESET_ALL)
            time.sleep(2)
            print("*E num piscar de olhos, o Humberto aparece, agarra você e te imobiliza")
            time.sleep(2)
            print(Fore.RED + "Raul: Você achou mesmo que eu não estava lhe esperando? Esperava um oponente que estivesse a altura de me vencer. Mas me enganei...")
            time.sleep(2)
            print("Raul: Mas admiro a sua coragem, apesar de sua burrice ser maior")
            time.sleep(2)
            print("Raul: eu poderia simplesmente te possuir agora, mas qual graça teria? Me diga aluno, o que deseja?")
            print(Style.RESET_ALL)
            decisao= input("A: Xingar ele."
                           " B: Pedir misericordia")
            while decisao !="A" and decisao != "B":
                print ("Responda com A ou B")
                decisao= input("A: Xingar ele."
                           " B: Pedir misericordia")
            if decisao == "A": #Desculpa pelo palavriado Raul
                print("VOCÊ: Vai se ****, prefiro morrer a pedir misericordia a você!")
                time.sleep(1)
                print(Fore.RED + "Raul: Como você desejar!")
                print(Style.RESET_ALL)
                time.sleep(1)
                print("e num piscar de olhos você desmaterializa.")
                time.sleep(3)
                jogo == False
        if jogo == False:
            time.sleep(2)
            print(derrota)
            break
        else:
            print("Você: Muito obrigado Raul, não sabia o que estava fazendo, quero que você atrase o EP apenas por alguns dias")
            time.sleep(1)
            print(Fore.RED + "Raul: Como você desejar! Porém, o adiamento será apenas para você, e não para seus colegas")
            print(Style.RESET_ALL)
            print (Fore.BLUE + "Boa sorte da próxima vez {}, seu finalizamento não foi 100%".format(nome_do_jogador))
            time.sleep(2)
            jogo == False
        if jogo == False:
            time.sleep(2)
            print(derrota)
            break