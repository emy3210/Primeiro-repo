def jogo():
    print("Bem vindo ao jogo do NIM! Escolha \n \n 1- Para jogar uma partida \n 2- Para jogar uma melhor de três")
    esc=int(input("O que você escolhe?"))
    if esc==1:
        print("Você escolheu jogar uma partida!")
        partida()

    elif esc==2:
        print("Você escolheu jogar um campeonato!")
        campeonato()




def partida():
    n=int(input("Quantas peças? "))
    m=int(input("Max de peças por rodada? "))
    print()
    if n%(m+1)==0:
        print("Você começa")
        j=usuario_escolhe_jogada(n,m)
        n=n-j
        print()
        print("Você tirou",j, "peças. \n Agora resta apenas", n, " peças no tabuleiro.")
    
    while n>0:
        print()
        i=computador_escolhe_jogada(n,m)
        n=n-i
        print("O computador tirou",i," peças. \n Agora restam", n, " peças no tabuleiro.")
        print()
        if n>0:    
            j=usuario_escolhe_jogada(n,m)
            n=n-j
            print("Você tirou",j, "peças. \n Agora resta apenas", n, " peças no tabuleiro.")
            print()
    print("Fim do jogo! O computador ganhou!")


#-------------------------------------------------------------------------------------------------------------------------------
def computador_escolhe_jogada(n,m):
    aux=n
    cont=0
    if m>=n:
        return n
    while aux%(m+1)!=0 and cont<m:
        cont=cont+1
        aux=n-cont
    if cont==0:
        cont=m
    return cont

#------------------------------------------------------------------------------------------------------------
def usuario_escolhe_jogada(n,m):
    j=int(input("Quantas peças você tira? "))
    while j>m or j<=0:
        print("Jogada inválida, tente de novo")
        print()
        j=int(input("Quantas peças você tira?"))
    print()
    return j




#---------------------------------------------------------------------------------------------------------------
def campeonato():
    for i in range(3):
        print()
        print("RODADA ",i+1)
        partida()  

    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")




jogo()
            
    
