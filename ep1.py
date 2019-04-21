# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Marcelo Miguel, marcelocm8@al.insper.edu.br
# - aluno B: Byron Hans, byronhboe@al.insper.edu.br

jogo = True
derrota = "GAME OVER! x___x "
#definição de todos os cenários

Hp=100
def procurar_cenários(): 
    cenário = {
        "Prédio 1":{ 
            "titulo":"Predio 1",
            "descrição":"Você está no Predio 1, aonde deseja ir?",
            "opções": {
                "Elevador":"Entrar no Elevador",
                "Biblioteca":"Entrar na Biblioteca"
            }
        },
        "Elevador":{
            "titulo": "Elevador",
            "descrição":"Você está no elevador, selecione um andar:",
            "opções": {
                "-1":"Ir para o Techlab",
                "4":"Ir para o andar das engenharias",
                "5":"Ir para o refeitorio",
            }
        },
        "-1":{
            "Titulo": "Techlab",
            "descrição":"Você está no Techlab, o habitat natural dos engenheiros"
                        "Um veterano do 9 semestre FULL PISTOlA te desafiou para um combate"
                        "Veterano(Ataque=20, Hp= 20)",
            "opções":{
                    "Atacar":"Atacar o veterano",
                    "Elevador":"voltar para o Elevador",
        },
        "4":{
            "Titulo": "Sala das Engenharias",
            "descrição":"Você está no quarto andar, o andar que habita o Raul"
                        "será que você é capaz de desafiar ele para uma batalha?"
                        "KITARA: Insperiano!, devo te alertar que, antes de chamar o Raul pro fight"
                        "tente passar no -1 andar primeiro"
                        "*Raul aparece*"
                        "Raul e seu assistente tão tudo cansado de ter corrigido as PI"
                        "Parece ser a hora perfeita para conseguir atrasar o EP",
        },
        "5":{
        }
        
                
    }
    return cenário


#início do código do jogo

jogo = True #o jogo funciona enquanto for true 
derrota = "GAME OVER! x__x "
Vitória = "Parabéns! Você venceu! Agora vá fazer o EP1! ¯\_(ツ)_/¯"

while jogo == True:
    
    print("KITARA: Olá Insperiano, meu nome é Kitara, sou um espectro"
      " invisível vindo de outra de dimensão. Fui enviada para porque você"
      " precisa conseguir adiar a entrega do EP1 de Design de Software senão"
      " senão você e todos os seus colegas vão pegar DP nessa matéria!!!"
      " Ficarei com você até conseguir, só então poderei voltar para minha"
      "dimensão!")
    
    print("")
    
    print(cenário["Prédio 1"])
    
    opção_1 = "A: Sair correndo com medo da Kitara."
    opção_2 = "B: Pedir para Kitara explicar melhor quem ela é."
    
    print("")
    
    print(opção_1)
    print(opção_2)
    
    escolha = input("Digite aqui a opção que deseja: ")
    
    print("")
    
    while escolha != "A" and escolha != "B": 
    
        print("Opção inválida, digite A ou B.")
        escolha = input("Digite aqui a opção que deseja: ")
        
    if escolha == "B":
        print("VOCÊ: Que diabos está acontecendo e como assim você é um"
           " espectro invisível de outra dimensão?! Eu tô ficando maluco?!")
        
        print("")
        
        print("KITARA: não há tempo para explicações Insperiano! Você precisa"
          "adiar o EP1 para o bem de todos! Aliás, qual o seu nome?")
        
        nome_do_jogador = input("Digite seu nome: ")
        print("")
        
        print("KITARA: Certo {},"
      " precisamos encontrar seu professor!".format(nome_do_jogador))
        
    elif escolha == "A": 
        print("Essa não, você correu para rua e morreu atropelado!")
        jogo = False
    elif jogo == False: 
        break
    
print(Vitória)