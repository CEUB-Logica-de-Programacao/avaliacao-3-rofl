# ## Questão 1
#
# Você foi contratado pela seleção brasileira para fazer uma análise sobre as seleções adversárias. Sua primeira tarefa
# consiste em realizar uma contagem de quantos jogadores possuem a altura máxima.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# [180, 166, 170, 180]
# ```
#
# A saída deve ser:
#
# ```
# 2
# ```
#
# Isso porque existem dois jogadores com altura máxima (180).
#
# Para obter a nota máxima dessa questão, deve-se utilizar apenas um ``for`` e nenhuma função pronta do Python.

def q1(heights):
    sorted_heights = []
    max = 0
    for i in heights: 
        if i > max:           
            sorted_heights.clear()
            max = i
        if i == max:
            sorted_heights.append(i)
    return len(sorted_heights)


if __name__ == '__main__':
    print(q1([180, 166, 170, 180]))
