import csv

def carregar_arquivo():
    try: 
        with open("processos.csv", "r") as arquivo:
            linhas = arquivo.readlines()
        return [linha.strip().split(",") for linha in linhas[1:]]
    except FileNotFoundError:
        print("Erro ao ler o arquivo.")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None