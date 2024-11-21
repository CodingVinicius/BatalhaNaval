def verificar(self, nome, linha, coluna, esquadraPC, esquadraPlayer, barcosPC, barcosPlayer):
        if nome != 'PC':  # Jogada do Jogador contra o PC
            if esquadraPC[linha][coluna] == 'Barc':
                parte_barco = (linha, coluna)
                esquadraPC[linha][coluna] = 'Acerto'
                for i in range(len(barcosPC)):
                    if barcosPC[i] == parte_barco:
                        if i % 2 == 0:
                            del barcosPC[i]
                            del barcosPC[i+1]  # Remove a próxima parte do barco
                        else:
                            del barcosPC[i]
                            del barcosPC[i-1]
            else:
                esquadraPC[linha][coluna] = 'Erro'

            if len(barcosPC) == 0:  # Vitória do Jogador
                return f'{nome} venceu o jogo, derrotando todas as embarcações!'

        if nome == 'PC':  # Jogada do PC contra o Jogador
            if esquadraPlayer[linha][coluna] == 'Barc':
                parte_barco = (linha, coluna)
                esquadraPlayer[linha][coluna] = "Acerto"
                for i in range(len(barcosPlayer)):
                    if barcosPlayer[i] == parte_barco:
                        if i % 2 == 0:
                            del barcosPlayer[i]
                            del barcosPlayer[i+1]  # Remove a próxima parte do barco
                        else:
                            del barcosPlayer[i]
                            del barcosPlayer[i-1]
            else:
                esquadraPlayer[linha][coluna] = 'Erro'

            if len(barcosPlayer) == 0:  # Vitória do PC
                return f'{nome} venceu o jogo, derrotando todas as embarcações!'