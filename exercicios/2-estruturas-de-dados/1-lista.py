# Crie uma lista apenas com elementos numéricos
list_num = [1, 2, 3, 4]
print(list_num)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
list_mista = ['Abobora', 2, [1, 2 , 3, 4], True, "Pato", 55, 3, False, 'Futebol', 'Macaco']
#print(len(list_mista),"\n",list_mista)

# Imprima na tela apenas os 5 primeiros elementos da lista
print(list_mista[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
list_mista[0:-1:2]
print(list_mista)

# Remova da lista o último item
list_mista.remove(True)
print(list_mista)

# Insira na lista um novo item
list_mista.append(21)
print(list_mista)

# Remova da lista um item específico
list_mista[3] = 0
print(list_mista)
