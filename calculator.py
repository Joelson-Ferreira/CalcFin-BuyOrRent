def calcular_valor_total_aluguel(valor_mensal_aluguel: float, taxa_aumento_aluguel: float, anos: int = 20) -> float:
  """
    Método responsável por calcular o valor do aluguel para determinado período
  """
  valor_total_aluguel = 0
  valor_mensal_aluguel_atual = valor_mensal_aluguel

  for _ in range(anos):
    valor_total_aluguel += 12 * valor_mensal_aluguel_atual
    valor_mensal_aluguel_atual *= (1 + taxa_aumento_aluguel/100)

  return round(valor_total_aluguel, 2)


def calcular_valor_total_investimento(valor_investimento: float, taxa_rendimento: float, anos: int = 20) -> float:
  """
      Método responsável por calcular o valor total de um investimento para determinado período
  """
  valor_total_investimento = valor_investimento * (1 + taxa_rendimento / 100) ** anos
  return round(valor_total_investimento, 2)


def calcular_valorizacao_imovel(valor_imovel: float, taxa_valorizacao: float, anos: int = 20) -> float:
  """
    Método responsável por calcular a valorização do imóvel para determinado período
  """
  valorizacao = valor_imovel * (1 + taxa_valorizacao / 100) ** anos - valor_imovel
  return round(valorizacao, 2)


def decisao_comprar_ou_alugar(valor_total_aluguel: float, valor_total_investido: float, valorizacao_imovel: float) -> str:
    """
      Método responsável por analisar os valores finais e decidir qual é mais vantajoso
    """
    valor_comparativo = valor_total_investido - valor_total_aluguel

    if valor_comparativo > valorizacao_imovel:
        return "alugar."
    elif valor_comparativo < valorizacao_imovel:
        return "comprar."
    else:
        return "ambas as opções são vantajosas."
