import pandas as pd

def resposta_1a(file_path):
    """Calcula os valores mínimos, médios e máximos da produção para cada animal em diferentes lactações."""
    df = pd.read_csv(file_path)
    df.columns = ['ID', 'Animal', 'Lactacao', 'dim', 'Producao']

    # Filtrando os dados para cada lactação
    lact_1 = df[df['Lactacao'] == 1]
    lact_2 = df[df['Lactacao'] == 2]
    lact_3_plus = df[df['Lactacao'] >= 3]

    # Inicializando uma lista para armazenar os resultados
    resultados = []

    # Calculando os valores mínimos, médios e máximos para cada animal em cada lactação
    for animal in df['Animal'].unique():
        # Filtrar os dados para o animal atual
        animal_lact_1 = lact_1[lact_1['Animal'] == animal]
        animal_lact_2 = lact_2[lact_2['Animal'] == animal]
        animal_lact_3_plus = lact_3_plus[lact_3_plus['Animal'] == animal]

        # Cálculos para a primeira lactação
        min_1 = animal_lact_1['Producao'].min() if not animal_lact_1.empty else float('nan')
        mean_1 = animal_lact_1['Producao'].mean() if not animal_lact_1.empty else float('nan')
        max_1 = animal_lact_1['Producao'].max() if not animal_lact_1.empty else float('nan')

        # Cálculos para a segunda lactação
        min_2 = animal_lact_2['Producao'].min() if not animal_lact_2.empty else float('nan')
        mean_2 = animal_lact_2['Producao'].mean() if not animal_lact_2.empty else float('nan')
        max_2 = animal_lact_2['Producao'].max() if not animal_lact_2.empty else float('nan')

        # Cálculos para a terceira ou mais lactações
        min_3_plus = animal_lact_3_plus['Producao'].min() if not animal_lact_3_plus.empty else float('nan')
        mean_3_plus = animal_lact_3_plus['Producao'].mean() if not animal_lact_3_plus.empty else float('nan')
        max_3_plus = animal_lact_3_plus['Producao'].max() if not animal_lact_3_plus.empty else float('nan')

        # Adicionando os resultados à lista
        resultados.append([
            animal, min_1, mean_1, max_1,
            min_2, mean_2, max_2,
            min_3_plus, mean_3_plus, max_3_plus
        ])

    # Criando o DataFrame com os resultados
    tabela_resultados = pd.DataFrame(resultados, columns=[
        'Animal',
        'Prod. Mínima - 1º Lact.', 'Prod. média - 1º Lact.', 'Prod. máxima - 1º Lact.',
        'Prod. Mínima - 2º Lact.', 'Prod. média - 2º Lact.', 'Prod. máxima - 2º Lact.',
        'Prod. Mínima - 3º+ Lact.', 'Prod. média - 3º+ Lact.', 'Prod. máxima - 3º+ Lact.'
    ])

    # Definindo opções de exibição do pandas para facilitar a leitura no terminal
    pd.set_option('display.max_columns', None)  # Mostrar todas as colunas
    pd.set_option('display.width', 1500)  # Ajustar a largura da exibição
    pd.set_option('display.float_format', '{:.2f}'.format)  # Formatar números com 2 casas decimais

    print("Resultado da Questão 1a:")
    print(tabela_resultados.to_string(index=False))  # Melhor para exibição no terminal

    # Salvando o DataFrame em um arquivo CSV
    tabela_resultados.to_csv('results/resultado_questao_1a.csv', index=False)

    return tabela_resultados


def resposta_1b(file_path):
    """Realiza o ajuste linear e calcula o erro quadrático médio para cada grupo."""
    df = pd.read_csv(file_path)
    df.columns = ['ID', 'Animal', 'Lactação', 'dim', 'Produção']

    def ajuste_linear(x, y):
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(x[i] ** 2 for i in range(n))
        denominator = (n * sum_x2 - sum_x ** 2)

        if denominator == 0:
            raise ValueError("Denominador zero encontrado na função de ajuste linear. Verifique se todos os valores de 'dim' são iguais.")
        
        a = (n * sum_xy - sum_x * sum_y) / denominator
        b = (sum_y - a * sum_x) / n
        return a, b

    def erro_quadratico_medio(x, y, a, b):
        n = len(x)
        eqm = sum((y[i] - (a * x[i] + b)) ** 2 for i in range(n)) / n
        return eqm

    resultados = []
    grupos = df.groupby(['Animal', 'Lactação'])

    for (animal_utilizado, lactacao_utilizado), grupo_utilizado in grupos:
        x_utilizado = grupo_utilizado['dim'].tolist()
        y_utilizado = grupo_utilizado['Produção'].tolist()

        try:
            a, b = ajuste_linear(x_utilizado, y_utilizado)
        except ValueError as e:
            print(f"Erro ao ajustar linearmente para o grupo ({animal_utilizado}, {lactacao_utilizado}): {e}")
            continue

        for (animal_alvo, lactacao_alvo), grupo_alvo in grupos:
            if (animal_utilizado, lactacao_utilizado) != (animal_alvo, lactacao_alvo):
                x_alvo = grupo_alvo['dim'].tolist()
                y_alvo = grupo_alvo['Produção'].tolist()

                eqm = erro_quadratico_medio(x_alvo, y_alvo, a, b)
                resultados.append([animal_utilizado, lactacao_utilizado, animal_alvo, lactacao_alvo, eqm])

    df_resultados = pd.DataFrame(resultados, columns=['Animal Utilizado', 'Lactação Utilizada', 'Animal Alvo', 'Lactação Alvo', 'EQM'])
    print(df_resultados)
    return df_resultados


def resposta_1c(file_path):
    """Verifica o desempenho da curva de cada animal quando aplicada para estimar a produção de outros animais."""
    df = pd.read_csv(file_path)
    df.columns = ['ID', 'Animal', 'Lactação', 'dim', 'Produção']

    def ajuste_linear(x, y):
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(x[i] ** 2 for i in range(n))
        denominator = (n * sum_x2 - sum_x ** 2)

        if denominator == 0:
            raise ValueError("Denominador zero encontrado na função de ajuste linear. Verifique se todos os valores de 'dim' são iguais.")
        
        a = (n * sum_xy - sum_x * sum_y) / denominator
        b = (sum_y - a * sum_x) / n
        return a, b

    def erro_quadratico_medio(x, y, a, b):
        n = len(x)
        eqm = sum((y[i] - (a * x[i] + b)) ** 2 for i in range(n)) / n
        return eqm

    resultados = []
    grupos = df.groupby(['Animal', 'Lactação'])

    for (animal_utilizado, lactacao_utilizado), grupo_utilizado in grupos:
        x_utilizado = grupo_utilizado['dim'].tolist()
        y_utilizado = grupo_utilizado['Produção'].tolist()

        try:
            a, b = ajuste_linear(x_utilizado, y_utilizado)
        except ValueError as e:
            print(f"Erro ao ajustar linearmente para o grupo ({animal_utilizado}, {lactacao_utilizado}): {e}")
            continue

        for (animal_alvo, lactacao_alvo), grupo_alvo in grupos:
            if (animal_utilizado, lactacao_utilizado) != (animal_alvo, lactacao_alvo):
                x_alvo = grupo_alvo['dim'].tolist()
                y_alvo = grupo_alvo['Produção'].tolist()

                eqm = erro_quadratico_medio(x_alvo, y_alvo, a, b)
                resultados.append([animal_utilizado, lactacao_utilizado, animal_alvo, lactacao_alvo, eqm])

    df_resultados = pd.DataFrame(resultados, columns=['Animal Utilizado', 'Lactação Utilizada', 'Animal Alvo', 'Lactação Alvo', 'EQM'])
    print(df_resultados)
    return df_resultados


def resposta_1d(file_path):
    """Calcula o erro médio para cada animal nas três lactações e identifica os animais com menor erro médio."""
    df = pd.read_csv(file_path)
    df.columns = ['ID', 'Animal', 'Lactação', 'dim', 'Produção']

    def ajuste_linear(x, y):
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(x[i] ** 2 for i in range(n))
        denominator = (n * sum_x2 - sum_x ** 2)
        
        if denominator == 0:
            raise ValueError("Denominador zero encontrado na função de ajuste linear. Verifique se todos os valores de 'dim' são iguais.")
        
        a = (n * sum_xy - sum_x * sum_y) / denominator
        b = (sum_y - a * sum_x) / n
        return a, b

    def erro_quadratico_medio(x, y, a, b):
        n = len(x)
        eqm = sum((y[i] - (a * x[i] + b)) ** 2 for i in range(n)) / n
        return eqm

    def calcula_erro_medio_por_lactacao(lactacao):
        resultados = []
        grupos = df[df['Lactação'] == lactacao].groupby(['Animal'])
        for (animal_utilizado, grupo_utilizado) in grupos:
            x_utilizado = grupo_utilizado['dim'].tolist()
            y_utilizado = grupo_utilizado['Produção'].tolist()
            
            try:
                a, b = ajuste_linear(x_utilizado, y_utilizado)
            except ValueError as e:
                print(f"Erro ao ajustar linearmente para o animal {animal_utilizado} na lactação {lactacao}: {e}")
                continue
            
            for (animal_alvo, grupo_alvo) in grupos:
                if animal_utilizado != animal_alvo:
                    x_alvo = grupo_alvo['dim'].tolist()
                    y_alvo = grupo_alvo['Produção'].tolist()
                    
                    eqm = erro_quadratico_medio(x_alvo, y_alvo, a, b)
                    resultados.append([animal_utilizado, lactacao, animal_alvo, eqm])
        
        df_resultados = pd.DataFrame(resultados, columns=['Animal Utilizado', 'Lactação', 'Animal Alvo', 'EQM'])
        erro_medio = df_resultados.groupby('Animal Utilizado')['EQM'].mean().reset_index()
        erro_medio = erro_medio.sort_values(by='EQM').reset_index(drop=True)
        return erro_medio

    resultados_1 = calcula_erro_medio_por_lactacao(1)
    resultados_2 = calcula_erro_medio_por_lactacao(2)
    resultados_3 = calcula_erro_medio_por_lactacao(3)

    return resultados_1, resultados_2, resultados_3

