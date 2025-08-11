# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

cursos_linkedin = ["python", "sql", "excel", "powerbi", "comunicacao"]

py = "python"
xlsx = "excel"
bi = "powerbi"

cursos_notas = {}

if py in cursos_linkedin:
    print(f"O curso {py} está na lista.")
    nota_py = int(input(f"Qual a nota para o curso {py}? "))
    cursos_notas[py] = nota_py
    
if xlsx in cursos_linkedin:
    print(f"O curso {xlsx} está na lista.")
    nota_xlsx = int(input(f"Qual a nota para o curso {xlsx}? "))
    cursos_notas[xlsx] = nota_xlsx
    
if bi in cursos_linkedin:
    print(f"O curso {xlsx} está na lista.")
    nota_bi = int(input(f"Qual a nota para o curso {bi}? "))
    cursos_notas[xlsx] = nota_bi
    
else:
    print("Curso não contém na lista")

print("Notas dos cursos:", cursos_notas)
