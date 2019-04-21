# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Marcelo Miguel, marcelocm8@al.insper.edu.br
# - aluno B: Byron Hans, byronhboe@al.insper.edu.br

# EP 2019-1: Escape Insper
#
## EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Marcelo Miguel, marcelocm8@al.insper.edu.br
# - aluno B: Byron Hans, byronhboe@al.insper.edu.br

jogo = True
derrota = "GAME OVER! x__x "
#definição de todos os cenários

cenário = {
        "Prédio 1":"Você está em frente ao prédio 1, o que deseja fazer?",
        "Elevador":"Você está no elevador, selecione um andar:"}


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