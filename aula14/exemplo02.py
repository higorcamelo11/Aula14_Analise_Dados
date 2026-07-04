# pip install fastparquet
import pandas as pd
import polars as pl
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Carregando...')
    
    # Lendo parquet - Leitura Direta
    # Pandas - 0:00:28.967092
    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    
    #  Polars - 0:00:09.937582
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    
    
    print(df_bolsa_familia.head())
    fim = datetime.now()
    print(f'Tempo de execução de {fim - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet: {e}')