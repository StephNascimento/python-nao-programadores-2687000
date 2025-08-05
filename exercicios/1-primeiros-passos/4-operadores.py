ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
resultado = ano_formatura - ano_nascimento
print(resultado)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
maior = ano_nascimento > ano_formatura
print(maior)
menor = ano_nascimento < ano_formatura
print(menor)
igual = ano_formatura == ano_nascimento
print(igual)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
com_a = 3 == 3 and 2 == 2
print(com_a)
com_b = 3 == 3 and 2 == 1
print(com_b)
com_c = 3 > 2 or 4 == 4
print(com_c)
com_d = 2 < 1 or 3 == 3
print(com_d)
com_e = not 3 == 1
print(com_e)
com_f = not 3 == 3
print(com_f)
