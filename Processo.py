class Processo:
    def __init__(self, pid, nome, prioridade, tempo_chegada=0, tempo_cpu_total=0):
        #Atributos 
        self.pid = pid
        self.nome = nome
        self.prioridade = prioridade
        self.tempo_chegada = tempo_chegada
        self.tempo_cpu_total = tempo_cpu_total
        
        #Variaveis de controle
        self.tempo_restante = tempo_cpu_total
        self.estado = "Nao Chegou"  #Estados possiveis: Nao Chegou, Pronto, Executando, Concluido
        self.tempo_espera = 0
        self.tempo_finalizacao = 0
        self.tempo_resposta = 0 #Também conhecido como Turnaround Time

    def __str__(self):
        return (f"PID: {self.pid}, Nome: {self.nome}, Prioridade: {self.prioridade}, "
                f"Chegada: {self.tempo_chegada}, CPU Total: {self.tempo_cpu_total}, "
                f"Restante: {self.tempo_restante}, Estado: {self.estado}")

        
    def executar(self, tempo_execucao):
        #Decrementa tempo restante do processo e altera estado p/ Concluido
        if self.tempo_restante > 0:
            self.tempo_restante -= tempo_execucao
            if self.tempo_restante <= 0:
                self.tempo_restante = 0
                self.estado = "Concluido"

    def atualizar_tempo_espera(self, tempo):
        #Incrementa o tempo que o processo passou na fila de prontos
        if self.estado == "Pronto":
            self.tempo_espera += tempo

    def finalizar(self, tempo_atual):
        #Calcula o tempo final quando o processo é concluído
        self.tempo_finalizacao = tempo_atual
        self.tempo_resposta = self.tempo_finalizacao - self.tempo_chegada
