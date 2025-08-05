resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"
print(resumo)

# Imprima na tela apenas a segunda letra da variável
resumo[1]
print(resumo[1])

# Imprima na tela a idade de Paloma (resposta esperada: "46")
resumo[23:26]
print(resumo[23:26])

# Imprima na tela o trecho final da variável
resumo[31:]
print(resumo[31:])

# Converta todos as letras para minúsculo e imprima na tela
resumo_lower = resumo.lower()
print(resumo_lower)

# Converta todas as letras para maiúscula e imprima na tela
resumo_upper = resumo.upper()
print(resumo_upper)

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela
resumo_title = resumo.title()
print(resumo_title)

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
resumo_capitalized = resumo.capitalize()
print(resumo_capitalized)

# Imprima na tela uma string utilizando uma variável, usando o recurso string format
idade = 46
print(f"Paloma tem {idade} anos e está estudando 'python'.")

