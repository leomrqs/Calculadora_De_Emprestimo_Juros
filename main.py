valor_emprestimo = 10000     # valor em reais R$
taxa_juros_mensal = 2        # % ao mês
prazo_meses = 12             # em meses
porcentagem_desconto = 0.10    # em porcentagem (0.01 - 0.99)

def valor_total(valor, juros_mensal, prazo):
    return valor * (1 + (juros_mensal/100)) ** prazo

def simulacao_desconto(valor, porcentagem):
    valor_descontado = valor * porcentagem
    montante = valor - valor_descontado
    return valor_descontado, montante


total = valor_total(valor_emprestimo, taxa_juros_mensal, prazo_meses)
parcela_mensal = total / prazo_meses
valor_desconto, montante = simulacao_desconto(total, porcentagem_desconto)

print(f"Montante final a ser pago: R${total:.2f}")
print(f"Valor de cada parcela mensal: R${parcela_mensal:.2f}")
print(f"Com o desconto, o montante seria de: R${montante:.2f}")
print(f"Economizando: R${valor_desconto:.2f}")