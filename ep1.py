# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Marcelo Miguel, marcelocm8@al.insper.edu.br
# - aluno B: Byron Hans, byronhboe@al.insper.edu.br

# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Marcelo Miguel, marcelocm8@al.insper.edu.br
# - aluno B: Byron Hans, byronhboe@al.insper.edu.br



#definição de todos os cenários

cenário = {
        "Prédio 1":"Você está em frente ao prédio 1, o que deseja fazer?",
        "Elevador":"Você está no elevador, selecione um andar:"}


#início do código do jogo

print("KITARA: Olá Insperiano, meu nome é Kitara, sou um espectro invisível vindo de"
      " outra de dimensão. Fui enviada para porque você precisa conseguir"
      " adiar a entrega do EP1 de Design de Software senão você e todos os"
      " seus colegas vão pegar DP nessa matéria!!! Ficarei com você até"
      " conseguir, só então poderei voltar para minha dimensão!")

print("")

print(cenário["Prédio 1"])

opção_1 = "A: Sair correndo com medo da Kitara."
opção_2 = "B: Pedir para Kitara explicar melhor quem ela é."

print("")

print(opção_1)
print(opção_2)

escolha = input("Digite aqui a opção que deseja: ")
print("")


if escolha == "A": 
    print("Essa não, você correu para rua e morreu atropelado!")
elif escolha == "B":
    print("VOCÊ: Que diabos está acontecendo e como assim você é um espectro"
           " invisível de outra dimensão?! Eu tô ficando maluco?!")
    print("")
    print("KITARA: não há tempo para explicações Insperiano! Você precisa"
          "adiar o EP1 para o bem de todos! Aliás, qual o seu nome?")
else:
    print("opção inválida por favor digite A ou B")

nome_do_jogador = input("Digite seu nome: ")

print("KITARA: Certo {},"
      " precisamos encontrar seu professor!".format(nome_do_jogador))
