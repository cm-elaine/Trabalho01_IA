import pandas as pd
import matplotlib.pyplot as plt
import os

## estou testando esta parte, não está no exercício pedido... é para 
# aprender um pouco mais e poder analisar as informações geradas!

def gerar_graficos(file_path, output_path):
    """Gera gráficos com base nos dados do arquivo CSV fornecido."""

    # Carregar os dados do CSV
    df = pd.read_csv(file_path)

    # Definir o estilo do gráfico
    plt.style.use('default')

    # Gráfico para produção mínima, média e máxima por lactação (Questão 1a)
    if 'Animal' in df.columns and 'Prod. Mínima - 1º Lact.' in df.columns:
        fig, ax = plt.subplots(figsize=(14, 8))
        df.plot(x='Animal', y=[
            'Prod. Mínima - 1º Lact.', 'Prod. média - 1º Lact.', 'Prod. máxima - 1º Lact.',
            'Prod. Mínima - 2º Lact.', 'Prod. média - 2º Lact.', 'Prod. máxima - 2º Lact.',
            'Prod. Mínima - 3º+ Lact.', 'Prod. média - 3º+ Lact.', 'Prod. máxima - 3º+ Lact.'
        ], kind='bar', ax=ax)

        plt.title('Produção de Leite por Animal e Lactação')
        plt.xlabel('Animal')
        plt.ylabel('Produção')
        plt.legend(title='Tipos de Produção')
        plt.xticks(rotation=90)
        plt.tight_layout()

        plt.savefig(os.path.join(output_path, 'grafico_questao_1a.png'))
        plt.close()

    # Gráficos para EQM por lactação (Questões 1b, 1c e 1d)
    elif 'Animal Utilizado' in df.columns and 'EQM' in df.columns:
        # Verifica se o arquivo contém a coluna 'Lactação Utilizada'
        if 'Lactação Utilizada' in df.columns:
            fig, ax = plt.subplots(figsize=(14, 8))
            for lactacao in df['Lactação Utilizada'].unique():
                df_lactacao = df[df['Lactação Utilizada'] == lactacao]
                df_lactacao.plot(x='Animal Utilizado', y='EQM', kind='bar', ax=ax, label=f'Lactação {lactacao}')

            plt.title('EQM por Animal e Lactação')
            plt.xlabel('Animal Utilizado')
            plt.ylabel('EQM')
            plt.legend(title='Lactações')
            plt.xticks(rotation=90)
            plt.tight_layout()

            plt.savefig(os.path.join(output_path, 'grafico_questao_1b.png'))
            plt.close()
        else:
            # Para os arquivos 1d_lactacao_1, 2 e 3, que não têm 'Lactação Utilizada'
            fig, ax = plt.subplots(figsize=(14, 8))
            df.plot(x='Animal Utilizado', y='EQM', kind='bar', ax=ax)

            plt.title('EQM por Animal')
            plt.xlabel('Animal Utilizado')
            plt.ylabel('EQM')
            plt.xticks(rotation=90)
            plt.tight_layout()

            if 'resultado_questao_1d_lactacao_1.csv' in file_path:
                plt.savefig(os.path.join(output_path, 'grafico_questao_1d_lactacao_1.png'))
            elif 'resultado_questao_1d_lactacao_2.csv' in file_path:
                plt.savefig(os.path.join(output_path, 'grafico_questao_1d_lactacao_2.png'))
            elif 'resultado_questao_1d_lactacao_3.csv' in file_path:
                plt.savefig(os.path.join(output_path, 'grafico_questao_1d_lactacao_3.png'))
            plt.close()

if __name__ == "__main__":
    # Caminho para os arquivos CSV com os resultados
    results_dir = r'C:\Users\elain\Desktop\Trabalho 01 - IA\results'

    # Gerar gráficos para cada arquivo CSV
    gerar_graficos(os.path.join(results_dir, 'resultado_questao_1a.csv'), results_dir)
    gerar_graficos(os.path.join(results_dir, 'resultado_questao_1b.csv'), results_dir)
    gerar_graficos(os.path.join(results_dir, 'resultado_questao_1c.csv'), results_dir)
    gerar_graficos(os.path.join(results_dir, 'resultado_questao_1d_lactacao_1.csv'), results_dir)
    gerar_graficos(os.path.join(results_dir, 'resultado_questao_1d_lactacao_2.csv'), results_dir)
    gerar_graficos(os.path.join(results_dir, 'resultado_questao_1d_lactacao_3.csv'), results_dir)
