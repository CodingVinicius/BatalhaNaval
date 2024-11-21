import random

class Jogo:
    def __init__(self):
        self.esquadra = None
        self.linhas = 6
        self.colunas = 6
        self.barcos = []

    def gerar_esquadra(self):
        self.esquadra = []
        
        for i in range(self.linhas):
            linha = []  
            for j in range(self.colunas):
                linha.append('Nada')  
            self.esquadra.append(linha)  

        return self.esquadra

    def AdicionarElementos(self):
        coordenadas = []
        cont = 0 

        while cont < 4:
            linha = random.randint(0, 5)
            coluna = random.randint(0, 5)
            parte1 = (linha, coluna)

            direcao = random.choice(['horizontal', 'vertical'])
            if coluna + 2 <= 5:
                if direcao == 'horizontal' and self.esquadra[linha][coluna + 1] != 'Barc' and self.esquadra[linha][coluna + 2] != 'Barc':
                    if parte1 not in coordenadas:
                        self.esquadra[linha][coluna] = 'Barc'
                        coordenadas.append(parte1)

                        coluna = coluna + 1

                        parte2 = (linha, coluna)
                        self.esquadra[linha][coluna] = 'Barc'
                        coordenadas.append(parte2)
                        cont += 1 
                        self.barcos.append(parte1)
                        self.barcos.append(parte2)
                            
            if linha + 2 <= 5:
                if direcao == 'vertical' and self.esquadra[linha + 1][coluna] != 'Barc' and self.esquadra[linha + 2][coluna] != 'Barc':
                    if parte1 not in coordenadas:
                        coordenadas.append(parte1)
                        self.esquadra[linha][coluna] = 'Barc'
                        linha = linha + 1

                        parte2 = (linha, coluna)
                        self.esquadra[linha][coluna] = 'Barc'
                        coordenadas.append(parte2)
                        cont += 1
                        
                        self.barcos.append(parte1)
                        self.barcos.append(parte2)

        return self.esquadra
    
    def retornar_embarcacoes(self):
        return self.barcos
    
    def verificar_coordenada(linha,coluna,tabuleiro):
        
        if tabuleiro[linha][coluna] =='Barc':
            return 'ACERTO'
        elif tabuleiro[linha][coluna] == 'Nada':
            return'ERRO'
        

        
    def marcar_embarcacoes(linha, coluna, embarcacoes):
        parte_barc = (linha, coluna)

        # Itera sobre a lista de embarcações
        for i in range(len(embarcacoes)):
            if embarcacoes[i] == parte_barc:
                # Remove ambas as partes do barco
                if i % 2 == 0:
                    parte2 = embarcacoes[i + 1]  # Parte seguinte
                else:
                    parte2 = embarcacoes[i - 1]  # Parte anterior
                
                embarcacoes.remove(parte_barc)
                embarcacoes.remove(parte2)
                break  # Interrompe após encontrar o 
        


class Jogador:
     def __init__(self, nome):
        self.nome = nome
        self.tabuleiro = None
        self.linha = None
        self.coluna = None


    


