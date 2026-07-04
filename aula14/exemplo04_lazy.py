import pandas as pd
import polars as pl
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Carregando...')
    
    # Lendo parquet - Leitura *Preguiçosa
    
    # Métodos que geram o plano de execução .lazy() e .scan_parquet()
    # lazy_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet').lazy()
    lazy_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    # print(lazy_bolsa_familia) Imprimindo o plano de execução
    
    lazy_bolsa_familia = lazy_bolsa_familia.select([
        'NOME MUNICÍPIO', 'VALOR PARCELA'
    ])
    
    lazy_bolsa_familia = lazy_bolsa_familia.group_by(
        'NOME MUNICÍPIO'
    ).agg(
        pl.col('VALOR PARCELA').sum()
    )
    
    lazy_bolsa_familia = lazy_bolsa_familia.sort(by='VALOR PARCELA', descending=True)
    
    df_bolsa_familia = lazy_bolsa_familia.collect() # Carrega os dados
    print(df_bolsa_familia.head())
    
    fim = datetime.now()
    print(f'Tempo de execução de {fim - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet: {e}')