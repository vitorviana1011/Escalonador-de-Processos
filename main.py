from arquivo import carregar_arquivo
from Processo import Processo

def escalonar_processo(fila_prontos, processo_em_execucao, tempo_atual, quantum):
    if processo_em_execucao and processo_em_execucao.estado == "Executando":
        # Se o processo em execução ainda não terminou, reinsere na fila
        if processo_em_execucao.tempo_restante > 0:
            fila_prontos.append(processo_em_execucao)

    # Ordena a fila por tempo_restante (SJF Preemptivo)
    fila_prontos.sort(key=lambda p: p.tempo_restante)

    # Round-Robin: Alterna entre os processos na fila
    if fila_prontos:
        return fila_prontos.pop(0)  # Retorna o próximo processo da fila

    return None  # Nenhum processo para executar

if __name__ == "__main__":

    lista_processos = []
    fila_prontos = []
    contador_concluidos = 0
    linha_do_tempo  = []
    tempo_atual = 0
    numero_de_processos = 0
    quantum = 2  # Tempo de quantum para o escalonamento Round-Robin

    arq = carregar_arquivo()

    if arq is not None:
        # Ordena os processos pela coluna de chegada (índice 2)
        ordem_processo = sorted(arq, key=lambda x: int(x[2]))

        # Cria instâncias de Processo e adiciona à lista
        for i, processo in enumerate(ordem_processo):
            pid = i + 1  # Gera um PID único para cada processo
            nome = processo[0]
            prioridade = int(processo[3])
            tempo_chegada = int(processo[2])
            tempo_execucao_total = int(processo[1])

            # Cria uma instância de Processo
            novo_processo = Processo(pid, nome, prioridade, tempo_chegada, tempo_execucao_total)
            lista_processos.append(novo_processo)

            numero_de_processos += 1

    else:
        print("Não foi possível carregar os dados.")

        while(contador_concluidos < numero_de_processos):
            # Adicionar processos a fila_prontos
            for processo in lista_processos:
                if processo.tempo_chegada <= tempo_atual and processo.estado == "Nao Chegou":
                    processo.estado = "Pronto"
                    fila_prontos.append(processo)
            # Decidir quem executar
            if fila_prontos or (processo_em_execucao and processo_em_execucao.tempo_restante > 0):
                processo_em_execucao = escalonar_processo(fila_prontos, processo_em_execucao, tempo_atual, quantum)

                # Executar o processo selecionado
                if processo_em_execucao:
                    processo_em_execucao.estado = "Executando"
                    tempo_executado = min(quantum, processo_em_execucao.tempo_restante)
                    processo_em_execucao.executar(tempo_executado)

                    # Verifica se o processo foi concluído
                    if processo_em_execucao.tempo_restante == 0:
                        processo_em_execucao.estado = "Concluído"
                        processo_em_execucao.finalizar(tempo_atual + tempo_executado)
                        contador_concluidos += 1
                        
            tempo_atual += 1

            pass