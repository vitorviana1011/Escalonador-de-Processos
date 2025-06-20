def gerar_relatorio(processos_concluidos, linha_do_tempo, nome_algoritmo):
    #Ordena os processos por nome para exibir
    processos_concluidos.sort(key=lambda p: p.nome)

    #Extrai o desempenho para facilitar a exibição
    nomes = [p.nome for p in processos_concluidos]
    tempos_cpu = [p.tempo_cpu_total for p in processos_concluidos]
    tempos_chegada = [p.tempo_chegada for p in processos_concluidos]
    tempos_espera = [p.tempo_espera for p in processos_concluidos]
    tempos_resposta = [p.tempo_resposta for p in processos_concluidos]
    
    print("\n" + "="*80)
    print(f"RELATÓRIO DE ESCALONAMENTO - {nome_algoritmo.upper()}")
    print("="*80)

    print("\nProcessos na Fila:")
    print("   " + "   ".join(f"{nome:<3}" for nome in nomes))

    print("\nTempo de CPU requerido pelos processos:")
    print("   " + "   ".join(f"{t:<3}" for t in tempos_cpu))

    print("\nTempo de Chegada dos processos:")
    print("   " + "   ".join(f"{t:<3}" for t in tempos_chegada))

    print("\n\nLINHA DO TEMPO\n")
    
    #Simplifica a linha do tempo com execuções consecutivas do mesmo processo
    timeline_simplificada = []
    if linha_do_tempo:
        timeline_simplificada.append(linha_do_tempo[0])
        for i in range(1, len(linha_do_tempo)):
            
            nome_proc_anterior = None
            if '---' in timeline_simplificada[-1]:
                nome_proc_anterior = timeline_simplificada[-1].split('---')[1].split('|')[0]

            nome_proc_atual = linha_do_tempo[i].split('---')[1].split('|')[0]

            if nome_proc_atual == nome_proc_anterior:
                tempo_final_atual = linha_do_tempo[i].rsplit('|',1)[-1]
                bloco_anterior = timeline_simplificada[-1].rsplit('|', 1)[0]
                timeline_simplificada[-1] = bloco_anterior + '|' + tempo_final_atual
            else:
                timeline_simplificada.append(linha_do_tempo[i])
    
    print("".join(timeline_simplificada))

    print("\n\nTempo de Espera de cada processo:")
    print("   " + "   ".join(f"{nome:<3}" for nome in nomes))
    print("   " + "   ".join(f"{t:<3}" for t in tempos_espera))

    print("\nTempo de Resposta de cada processo:")
    print("   " + "   ".join(f"{nome:<3}" for nome in nomes))
    print("   " + "   ".join(f"{t:<3}" for t in tempos_resposta))

    #Calcula e exibe as médias
    if processos_concluidos:
        tempo_medio_espera = sum(tempos_espera) / len(tempos_espera)
        tempo_medio_resposta = sum(tempos_resposta) / len(tempos_resposta)
        print(f"\n\nTempo Médio de Resposta: {tempo_medio_resposta:.2f}")
        print(f"Tempo Médio de Espera: {tempo_medio_espera:.2f}")
    
    print("="*80 + "\n")
