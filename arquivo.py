import csv

#Lê processos de um arquivo CSV especificado
def carregar_processos_do_csv(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
            next(arquivo)  #Pula a linha do cabeçalho
            leitor_csv = csv.reader(arquivo)
            return [linha for linha in leitor_csv if linha] #Ignora linhas vazias
    except FileNotFoundError:
        print(f"ERRO: Arquivo '{nome_arquivo}' não encontrado")
        return None
    except Exception as e:
        print(f"ERRO inesperado ao ler o arquivo '{nome_arquivo}': {e}")
        return None
