import pandas as pd
import polars as pl
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Carregando...')
    
    # Uso do pl.Categorical() para melhorar a performance da RAM
    # with StringCache():
    # Uso do pl.Categorical() para comparar os municípios repetidos 
    df_scan = (
        pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
        .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])
        # Convertendo município p/ Categorical
        .with_columns([
            pl.col('NOME MUNICÍPIO').cast(pl.Categorical)
        ])
        .group_by('NOME MUNICÍPIO')
        .agg(pl.col('VALOR PARCELA').sum())
        .sort('VALOR PARCELA', descending=True)
    )
    
    df_bolsa_familia = df_scan.collect()
    print(df_bolsa_familia.head())
    
    fim = datetime.now()
    print(f'Tempo de execução de {fim - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet: {e}')