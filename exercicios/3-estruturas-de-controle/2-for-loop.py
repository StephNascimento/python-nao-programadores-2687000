# Crie uma lista
lista = ["banana", "maçã", "pera", "uva", "batata", "alho"]

# Crie um for loop para imprimir cada elemento dessa lista
for fruta in lista:
    print(fruta)

# Crie um objeto iterável utilizando a função range()
list(range(7))
list(range(2,40,2))

# Use esse objeto iterável para criar um for loop que imprima na tela a frase "Estou aprendendo uma linguagem de programação."
for num in range(7):
    print(f"{num}  - Estou aprendendo uma linguagem de programação")

for item in list(range(2,40,2)):
    print(item, "- Estou aprendendo uma linguagem de programação")
