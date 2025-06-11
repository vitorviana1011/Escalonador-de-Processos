class Processo:
    def __init__(self, pid, nome, prioridade, tempo_chegada=0, tempo_cpu_total=0):
        self.pid = pid  # Identificador único do processo
        self.nome = nome 
        self.prioridade = prioridade 
        self.tempo_chegada = tempo_chegada 
        self.tempo_cpu_total = tempo_cpu_total
        self.tempo_restante = tempo_cpu_total  
        self.estado = "Nao Chegou"  
        self.tempo_espera = 0  # Tempo acumulado na fila de prontos
        self.tempo_finalizacao = 0  # Instante de tempo em que o processo foi finalizado
        self.tempo_retorno = 0  # Tempo de retorno (tempo finalização - tempo chegada)

    def __str__(self):
        return (f"PID: {self.pid}, Nome: {self.nome}, Prioridade: {self.prioridade}, "
                f"Tempo de Chegada: {self.tempo_chegada}, Tempo CPU Total: {self.tempo_cpu_total}, "
                f"Tempo Restante: {self.tempo_restante}, Estado: {self.estado}, "
                f"Tempo de Espera: {self.tempo_espera}, Tempo de Finalização: {self.tempo_finalizacao}, "
                f"Tempo de Retorno: {self.tempo_retorno}")

    def executar(self, tempo):
        #Executa o processo por um determinado tempo.
        if self.estado == "NAO CHEGOU":
            raise ValueError("O processo ainda não chegou.")
        if self.estado == "Concluído":
            raise ValueError("O processo já foi concluído.")
        
        self.estado = "Executando"
        self.tempo_restante -= tempo
        if self.tempo_restante <= 0:
            self.tempo_restante = 0
            self.estado = "Concluído"

    def atualizar_tempo_espera(self, tempo):
        #Atualiza o tempo de espera do processo.
        if self.estado == "Pronto":
            self.tempo_espera += tempo

    def finalizar(self, tempo_atual):
        #Finaliza o processo e calcula os tempos relacionados.
        if self.estado != "Concluído":
            raise ValueError("O processo ainda não foi concluído.")
        self.tempo_finalizacao = tempo_atual
        self.tempo_retorno = self.tempo_finalizacao - self.tempo_chegada