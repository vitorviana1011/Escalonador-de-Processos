import copy
from relatorio import gerar_relatorio

def simulacao_round_robin(lista_processos_inicial, quantum):

    #Cria uma copia para não modificar a lista original
    processos = copy.deepcopy(lista_processos_inicial)
    
    tempo_atual = 0
    fila_prontos = []
    processos_concluidos = []
    processo_em_execucao = None
    tempo_no_quantum = 0
    linha_do_tempo = [f"|{tempo_atual}|"]
    num_processos = len(processos)

    #O loop principal continua enquanto houver processos não concluídos
    while len(processos_concluidos) < num_processos:
        
        #Adiciona processos a fila de prontos conforme eles chegam
        for p in processos:
            if p.estado == "Nao Chegou" and p.tempo_chegada <= tempo_atual:
                p.estado = "Pronto"
                fila_prontos.append(p)
        
        #Se o processo em execução estourou o quantum, ele é mandado de volta pra fila
        if processo_em_execucao and tempo_no_quantum == quantum:
            if processo_em_execucao.tempo_restante > 0: #Só volta pra fila se não terminou
                processo_em_execucao.estado = "Pronto"
                fila_prontos.append(processo_em_execucao)
            linha_do_tempo.append(f"---{processo_em_execucao.nome}---|{tempo_atual}|")
            processo_em_execucao = None
        
        #Aloca a CPU se estiver ociosa e houver processos prontos
        if not processo_em_execucao and fila_prontos:
            processo_em_execucao = fila_prontos.pop(0)
            processo_em_execucao.estado = "Executando"
            tempo_no_quantum = 0 # Reseta o contador do quantum

        #Atualiza o tempo de espera para todos os processos na fila de prontos
        for p in fila_prontos:
            p.atualizar_tempo_espera(1)

        #Executa o processo alocado na CPU por uma unidade de tempo
        if processo_em_execucao:
            processo_em_execucao.executar(1)
            tempo_no_quantum += 1
            if processo_em_execucao.estado == "Concluido":
                processo_em_execucao.finalizar(tempo_atual + 1)
                processos_concluidos.append(processo_em_execucao)
                linha_do_tempo.append(f"---{processo_em_execucao.nome}---|{tempo_atual + 1}|")
                processo_em_execucao = None
        
        #Avança o relógio
        tempo_atual += 1

    #Gera o relatório
    gerar_relatorio(processos_concluidos, linha_do_tempo, f"Round-Robin (Quantum={quantum})")
