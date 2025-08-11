# Declare 4 variáveis do tipo numérica
a = 10
b = 4
c = 7
d = 15

# Crie uma estrutura condicional para comparar dois números
if a > b:
    print(f"A condição é verdadeira: {a} é maior que {b}")
else:
    print(f"A condição é falsa: {a} não é maior que {b}")

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
if c == 7:
    print(f"A condição é cumprida: {c} é igual a 7")

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
else:
    print(f"A condição não é cumprida: {c} não é igual a 7")

# Insira outras condições na estrutura condicional usando o elif
if c == 7:
    print(f"A condição é cumprida: {c} é igual a 7")
elif d > 10:
    print(f"A condição é cumprida: {d} é maior que 10")
else:
    print(f"A condição não é cumprida: {d} não é maior que 10")

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if c == 7 and d > 10:
    print(f"A condição é cumprida: {c} é igual a 7 e {d} é maior que 10")
else:
    print(f"A condição não é cumprida: {c} não é igual a 7 e {d} não é maior que 10")

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if c > b or d > a:
    print(f"A condição é cumprida: {c} é maior que {b} ou {d} é maior que {a}")
