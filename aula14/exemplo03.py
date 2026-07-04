# pip install fastparquet
import pandas as pd
import polars as pl
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Carregando...')
    
    # Lendo parquet - Leitura *Preguiçosa scan_parquet
    # scan_parquet - gera um plano de execução. Não traz os dados.
    df_scan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    # print(df_scan)  # printa o Plano de execução
    
    # pré-processamento ...
    
    # .Collect executa o plano, carregando os dados p/ a memória. 
    df_bolsa_familia = df_scan.collect()
    print(df_bolsa_familia.head())  
    
    
    
    fim = datetime.now()
    print(f'Tempo de execução de {fim - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet: {e}')