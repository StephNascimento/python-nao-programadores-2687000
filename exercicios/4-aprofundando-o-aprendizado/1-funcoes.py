# Crie uma função para selecionar o curso desejado em uma trilha profissional

def selecionar_curso():
    curso = int(input('Digite o número do curso que você deseja iniciar: 1-Python, 2-Excel, 3-PowerBI 2'))
    return curso

# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
def percorre_curso(curso_selecionado):
    trilha = {1: {'titulo': 'Python', 'total_niveis': 3},
              2: {'titulo': 'Excel', 'total_niveis': 7},
              3: {'titulo': 'PowerBI', 'total_niveis': 5}}
    
    curso_atual = trilha[curso_selecionado]['titulo']
    curso_nivel_atual = 1
    curso_total_niveis = trilha[curso_selecionado]['total_niveis']

    print(f"Bem-vindo ao curso {curso_atual}!. Você está iniciando o curso no nível {curso_nivel_atual}.\n")

    while curso_nivel_atual <= curso_total_niveis:
        print(f'Parabéns! Você acaba de finalizar a fase {curso_nivel_atual} do curso {curso_atual}.\n')
        curso_nivel_atual += 1
    else:
        print(f'Você concluiu o curso {curso_atual} com sucesso!')
# Execute as funções

curso = selecionar_curso()
percorre_curso(curso) 
