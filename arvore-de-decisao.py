# ==================================================================
# ÁRVORE DE DECISÃO DE CRÉDITO
# ==================================================================

print("########## 1. Coleta de dados ###########")
nome_empresa = input("Nome da empresa: ")
faturamento_mensal = float(input("Faturamento mensal: "))
valor_emprestimo = float(input("Valor do empréstimo solicitado: "))

print("\n########## 2. Cálculo da parcela (em 12 vezes sem juros) ###########")
parcela_mensal = valor_emprestimo / 12
print(f"Valor da parcela mensal: R$ {parcela_mensal:.2f}")

print("\n########## 3. Como é calculado ###########")
# O cálculo da porcentagem é direto, pois a fórmula é a mesma
porcentagem_parcela = (parcela_mensal / faturamento_mensal) * 100

print("\n########### 4. Árvore de decisão ###########")
if porcentagem_parcela <= 30:
    print("✅ APROVADO!")
elif porcentagem_parcela <= 50:
    print("⚠️ EM ANÁLISE! (Risco moderado)")
else:
    print("❌ RECUSADO!")

print("\n########## 5. Resumo da análise ###########")
print(f"Empresa: {nome_empresa}")
print(f"Faturamento mensal: R$ {faturamento_mensal:.2f}")
print(f"Valor do empréstimo solicitado: R$ {valor_emprestimo:.2f}")
print(f"Valor da parcela mensal: R$ {parcela_mensal:.2f}")
print(f"Porcentagem da parcela em relação ao faturamento: {porcentagem_parcela:.2f}%")