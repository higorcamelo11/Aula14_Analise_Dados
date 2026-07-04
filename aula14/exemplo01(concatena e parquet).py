# import pandas as pd
import polars as pl
from datetime import datetime
import os

ENDERECO_DADOS = './../DADOS/'


try:
    inicio = datetime.now()
    print('Obtendo dados...')
    
    
    df_bolsa_familia = None
    lista_arquivos = []
    
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
    
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)
        
    # print(lista_arquivos)
        
    for nome in lista_arquivos:
        print(f'Processando o arquivo {nome} ...')
        
        # 0:05:03.665336 - Pandas
        # df = pd.read_csv(ENDERECO_DADOS + nome, sep=';', encoding='iso-8859-1')
        # 0:00:34.748581 - Polars
        df = pl.read_csv(ENDERECO_DADOS + nome, separator=';', encoding='iso-8859-1')
        
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            # df_bolsa_familia = pd.concat([df_bolsa_familia, df])
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
            
            
        del df
        
        print(f'Arquivo {nome} processado com sucesso!')
        print(df_bolsa_familia.head())
        
        
    print(df_bolsa_familia.columns)
    
    # Converter a série VALOR PARCELA
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64())
    )
    
    print('Iniciando a gravação do arquivo parquet...')
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    
    print('\nGravação do arquivo parquet concluída com sucesso!')
    print(df_bolsa_familia.head())
    print(df_bolsa_familia.shape)
    
    fim = datetime.now()
    print(f'Tempo de execução de {fim - inicio}')
    
except Exception as e:
    print(f'Erro ao obter dados - {e}')