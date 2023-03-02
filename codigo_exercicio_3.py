faturamento_mensal = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]

# Calcula o menor e o maior valor de faturamento
valores_faturamento = [dia['valor'] for dia in faturamento_mensal if dia['valor'] != 0.0]
menor_valor = min(valores_faturamento)
maior_valor = max(valores_faturamento)

# Calcula a média de faturamento, ignorando os dias sem faturamento
valores_faturamento_sem_zero = [dia['valor'] for dia in faturamento_mensal if dia['valor'] != 0.0]
media_mensal = sum(valores_faturamento_sem_zero) / len(valores_faturamento_sem_zero)

# Calcula o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_media = sum([1 for dia in faturamento_mensal if dia['valor'] > media_mensal])

# Exibe os resultados
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)

 
