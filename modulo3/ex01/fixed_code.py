import json
import random
from datetime import datetime
import math as m

class   Humano:
  def __init__(self, nome, idade = 40, cidade="São Paulo",     active=True):
    self.nome=nome
    self.idade=idade
    self.cidade=cidade
    self.active = active
    self.criado_em = datetime.now()
    self.contador=0

  def processar_dados( self, dados,  filtro=None ):
        """Processa os dados e retorna o resultado"""
        resultados = []
        # TODO: Adicionar validação para o parâmetro 'dados'

        for item in dados:
          if filtro and item not in filtro:
            continue
          if type(item) is not str:
             item = str(item)
          item = item.strip()
          if len(item) > 0:
            resultados.append(item.upper())
            self.contador+=1
          else:
                print("Item vazio encontrado!")



        return resultados

  def calcular_estatisticas(self, numeros):
    """Calcula algumas estatísticas básicas"""
    if len(numeros) == 0:
        return None
    soma = sum(numeros)
    media = soma / len(numeros)
    variancia = sum([(x - media)**2 for x in numeros]) / len(numeros)
    desvio_padrao = m.sqrt(variancia)

    resultado = {"soma": soma,
               "media": media,
           "variancia": variancia,
      "desvio_padrao": desvio_padrao}

    return     resultado


def gerar_relatorio(dados, nome_arquivo, formato="json"):
    """Gera um relatório com base nos dados fornecidos."""
    if formato != "json" and formato != "csv" and formato != "txt":
      raise ValueError(f"Formato inválido: {formato}")

    if not isinstance(dados, list):
        dados = [dados]

    if formato == "json":
        with open(nome_arquivo, "w") as f:
            json.dump(dados, f, indent=4)
    elif formato == "csv":
        with open(nome_arquivo, "w") as f:
            # Implementação CSV
            header = ",".join(dados[0].keys()) if dados and isinstance(dados[0], dict) else ""
            f.write(header + "\n")

            for item in dados:
                if isinstance(item, dict):
                    linha = ",".join([str(v) for v in item.values()])
                    f.write(linha + "\n")
    else:
        with open(nome_arquivo, "w") as f:
            for item in dados:
                f.write(str(item) + "\n")
    print(f"Relatório gerado com sucesso! Arquivo: {nome_arquivo}")
    return True


def calculo_de_resultado(a, b, c, d=10, e=None, f=False):
    resultado = 0
    if a > 0 and b > 0 and c > 0:
        if 'f' == True:
            if e is not None:
                resultado = a * b * c * d * e
            else:
                resultado = a * b * c * d
        else:
            for i in range(0, a):
                for j in range(0, b):
                    for k in range(0, c):
                        if i % 2 == 0 and j % 2 == 0 and k % 2 == 0:
                            resultado += 1
                        elif i % 3 == 0 and j % 3 == 0 and k % 3 == 0:
                            resultado += 2
                        else:
                            resultado += 0.5
    return resultado


def gerar_grafico(dados):
    pass


X = 100
Y = 200
z = X + Y

LISTA_DE_ITENS = [
    "item1",
    "item2",
    "item3",
    "item4",
"item5"]

if __name__ == "__main__":
    numeros = [random.randint(1, 100) for _ in range(50)]
    projeto = Humano(nome="Teste", idade=25)
    estatisticas = projeto.calcular_estatisticas(numeros)
    dados_processados = projeto.processar_dados(["a", "b", "c", "", "d", 1, 2, 3])

    print(f"Contador: {projeto.contador}")
    print(f"Estatísticas: {estatisticas}")
    print(f"Dados processados: {dados_processados}")

    gerar_relatorio(estatisticas, "relatorio.json")

    for i in range(10):
        pass