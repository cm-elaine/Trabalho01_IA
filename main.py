from utils import resposta_1a, resposta_1b, resposta_1c, resposta_1d

# Caminho para o dataset
file_path = r'C:\Users\elain\Desktop\Trabalho 01 - IA\dataset.csv'

# Processar e exibir o resultado da questão 1a
resultado_1a = resposta_1a(file_path)
print("Resultado da Questão 1a:")
print(resultado_1a)
resultado_1a.to_csv('results/resultado_questao_1a.csv')

# # Processar e exibir o resultado da questão 1b
# resultado_1b = resposta_1b(file_path)
# print("Resultado da Questão 1b:")
# print(resultado_1b)
# resultado_1b.to_csv('results/resultado_questao_1b.csv')

# # Processar e exibir o resultado da questão 1c
# resultado_1c = resposta_1c(file_path)
# print("Resultado da Questão 1c:")
# print(resultado_1c)
# resultado_1c.to_csv('results/resultado_questao_1c.csv')

# # Processar e exibir o resultado da questão 1d
# resultado_1d_1, resultado_1d_2, resultado_1d_3 = resposta_1d(file_path)
# print("Resultado da Questão 1d - Lactação 1:")
# print(resultado_1d_1)
# resultado_1d_1.to_csv('results/resultado_questao_1d_lactacao_1.csv')

# print("Resultado da Questão 1d - Lactação 2:")
# print(resultado_1d_2)
# resultado_1d_2.to_csv('results/resultado_questao_1d_lactacao_2.csv')

# print("Resultado da Questão 1d - Lactação 3:")
# print(resultado_1d_3)
# resultado_1d_3.to_csv('results/resultado_questao_1d_lactacao_3.csv')
