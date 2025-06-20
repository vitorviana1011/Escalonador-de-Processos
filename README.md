# Escalonador-de-Processos
Um simulador de processos realizado para a disciplina de Sistemas Operacionais

Escalonador de Curto prazo:
Mudança de Estados do processos: 
-execução -> estado de espera -> pronto 
ou qualquer outra variação desse tipo de processo, por exemplo:
-execução -> tempo de execução expirou  -> estado de espera -> execução -> pronto


SJF preemptivo
O algoritmo de escalonamento conhecido como menor tarefa primeiro (SJF - Shortest Job First) consiste em atribuir o processador à menor (mais curta) tarefa da fila de tarefas prontas, o preemptivo implica que INTERROMPE um processo para começar um de mais curta duração. Vídeo explicativo:
https://www.youtube.com/watch?v=OVWc4wDX1u4



Round Robin
Fila cíclica: Mantém-se uma fila (FIFO) de processos prontos. Quando um processo chega, enfileira-se no fim. O escalonador retira do início, deixa executar até quantum ou término, e:
-Se terminou: registra o término e calcula métricas.
-Se não terminou: decrementa restante, re-enfileira no fim.




