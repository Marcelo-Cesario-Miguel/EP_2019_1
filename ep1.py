# EP 2019-1: Escape Insper
#
# Alunos:
# - aluno A: Marcelo Miguel, marcelocm8@al.insper.edu.br
# - aluno B: Byron Hans, byronhboe@al.insper.edu.br


#definição de todos os cenários

# Python program to print 
# red text with green background 
  
from colorama import Fore, Back, Style 
 
cenário = {
        "Prédio 1":"Você está em frente ao prédio 1, o que deseja fazer?",
        "Elevador":"Você está no elevador, selecione um andar:",
        "Saguão":"Vocês tá no saguão do prédio 1, o que deseja fazer?", 
        "Biblioteca":"Você está na biblioteca do olhar penetrante"}



#início do código do jogo
vida = 100
vida_boss = 1000
import time
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
    time.sleep(3)
    
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
            print(Fore.BLUE + "KITARA: essa não, forças inimigas interdimensionais estão"
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
                  " EU estou invisível também?")
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
        print("Você está na entrada da biblioteca e novamente as pessoas"
              " te olham feio brevemente antes de retomar o que faziam.")
        print('')
        time.sleep(2)
        print("Você percebe que tem um veterano te que conitnuo te encarando.")
        
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
            print ("KITARA: Nãooo! Não corra, ele se você correr você morre!")
            print('')
            time.sleep(2)
            print("O veterano te alcançou, entrou dentro do seu corpo,"
                  " consumiu sua alma e você caiu duro, como se fosse um"
                  " infarto fulminante.")
            print('')
            jogo = False
        
        elif jogo == False:
            break
        
        else:
            print(" O veterano  olhou bem no fundo dos seus olhos e te levou"
                  " para uma outra dimensão. Vocês estavam num campo de"
                  " batalha!")
            print('')
            time.sleep(2)
            print("VOCÊ: Meu Deus! Onde eu estou?! Como eu vim parar aqui?!")
            print('')
            time.sleep(2)
            print("KITARA: essa não, o veterano possuido de te invocou para"
                  " uma dimensão de guerra! Você terá que lutar com ele!")
            print('')
            time.sleep(2)
            print("VOCÊ: como assim eu vou ter que lutar?!")
            print('')
            time.sleep(2)
            print("KITARA: Você faz muitas perguntas! Controle o medo!"
                  " Preste bem atenção você tem 100 pontos de vida"
                  " se você perder esses 100 pontos, vc morre e estará tudo"
                  " acabado! Não deixei o seu inimigo te acertar!"
                  " Nessa dimensão eu tenho o poder de forjar um único"
                  " equipamento para você lutar!")
            
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
                    
            print ("KITARA: agora que você escolheu seu equipamento,"
                   "lute como um bravo guerreiro!")
            time.sleep(2)
            print('')
            print("VOCÊ: Meu Deus do céu que coisa maluca mas"
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
                print("Dano causado: 700")
                print('')
                print("HP - {}: ".format(nome_do_jogador))
                print(vida)
                print('')
                print("HP - O Veterando Sugador de Almas: ")
                print(vida_boss)
                print('')   
                jogo = False
            
            elif jogo == False:
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
                
                
                
                
            
                
                

    
print(derrota) 
