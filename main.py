#PROJETO DE SISTEMAS OPERACIONAIS 
#Alunos: João Antonio Sitta Martins e Vitor Viana

import sys
from Processo import Processo
from arquivo import carregar_processos_do_csv
from SJF_preemptivo import simulacao_sjf_preemptivo
from Round_Robin import simulacao_round_robin

def main():
    #Carrega os dados do arq CSV
    dados_processos = carregar_processos_do_csv("processos2.csv")

    if not dados_processos:
        print("Nenhum processo foi carregado. Encerrando o programa.")
        sys.exit(1) 
        
    #Converte os dados em uma lista de objetos da classe Processo
    lista_processos_base = []
    for i, p_info in enumerate(dados_processos):
        try:
            novo_processo = Processo(
                pid=i + 1,
                nome=p_info[0].strip(),
                tempo_cpu_total=int(p_info[1]),
                tempo_chegada=int(p_info[2]),
                prioridade=int(p_info[3])
            )
            lista_processos_base.append(novo_processo)
        except (ValueError, IndexError) as e:
            print(f"Aviso: Ignorando linha mal formatada no CSV: {p_info}. Erro: {e}")

    #Ordena a lista de processos pelo tempo de chegada
    lista_processos_base.sort(key=lambda p: p.tempo_chegada)

    #Executa o SJF Preemptivo
    print("\n--- INICIANDO SIMULAÇÃO SJF PREEMPTIVO ---")
    simulacao_sjf_preemptivo(lista_processos_base)

    #Executa o algoritmo Round-Robin com quantum = 5
    print("\n--- INICIANDO SIMULAÇÃO ROUND-ROBIN ---")
    simulacao_round_robin(lista_processos_base, quantum=5)

    print("Todas as simulações foram concluídas.")

if __name__ == "__main__":
    main()
