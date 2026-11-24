# 5. Validador de Idade para Contratação
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(idade <= 24)