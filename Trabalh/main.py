from BatalhaNaval import Jogo, Jogador
import random

def main():

    jogadas_pc = []
    jogadas_player= []

    jogo = Jogo()

    pc = Jogador('PC')
    player =  Jogador('Marcus')

    player.tabuleiro = jogo.gerar_esquadra()
    player.tabuleiro = jogo.AdicionarElementos()
    def computador():

        pc.tabuleiro = jogo.gerar_esquadra()
        pc.tabuleiro = jogo.AdicionarElementos()
        barcos_pc = jogo.retornar_embarcacoes()
        pc.linha = random.randint(0,15)
        pc.coluna =  random.randint(0,15)

        jogada =(pc.linha,pc.coluna)

        if jogada not in jogadas_pc:
            res =  jogo.verificar_coordenada(pc.linha,pc.coluna,pc.tabuleiro)
            if res == 'ACERTO':
                tabuleiro_pc[pc.linha][pc.coluna] = 'ACERTO'
                remocao =  jogo.marcar_embarcacoes(pc.linha, pc.coluna, barcos_pc)
            elif res == 'ERRO':
                tabuleiro_pc[pc.linha][pc.coluna] = 'ERRO'

            print(f"{player.nome} Tabuleiro:")
            for linha in tabuleiro_pc:
                print(linha)
            print("\n")

        


    tabuleiro_pc = jogo.gerar_esquadra()
    tabuleiro_player = jogo.gerar_esquadra()








    print(f"{player.nome} Tabuleiro:")
    for linha in tabuleiro_pc:
        print(linha)

    print("\n")

    print(f"{pc.nome} Tabuleiro:")
    for linha in tabuleiro_player:
        print(linha)
