# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.
# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {}

estudante['nome'] = input('Qual seu nome? ')
estudante['ano_conheceu_linkedin'] = int(input('Que ano você conheceu o linkedin? '))
estudante['ano_atual'] = int(input('Que ano estamos? '))
cursos = input('Quais foram os cursos que você realizou no linkedin learning? (Separe-os com vírgula) ')

estudante['cursos'] = cursos.split(', ')

total_anos = estudante['ano_atual'] - estudante['ano_conheceu_linkedin']
total_cursos = len(estudante['cursos'])

print(f'''Olá {estudante['nome']}, desde {estudante['ano_conheceu_linkedin']} você conhece o LinkedIn. Nesses {total_anos} anos, 
você realizou {total_cursos} cursos, sendo o primeiro curso {estudante['cursos'][0]} e o último curso {estudante['cursos'][-1]}''')
