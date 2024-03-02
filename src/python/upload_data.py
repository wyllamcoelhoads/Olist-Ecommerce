# %%

import os 
import pandas as pd
import sqlalchemy


#Os endereços do projeto e de sub pastas
BASE_DIR = os.path.dirname( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ))
DATA_DIR = os.path.join( BASE_DIR, 'data' )

# Uma forma elegante de encontrar os arquivos de dados        
files_names = [ i for i in os.listdir( DATA_DIR ) if i.endswith('.csv') ] # Compresão de Listas - List Compression

# Abrindo conexão com banco...
str_connection = 'sqlite:///{path}'
str_connection = str_connection.format( path = os.path.join( DATA_DIR, 'olist.db') )
connection = sqlalchemy.create_engine( str_connection )

# Para cada arquivo é realizado uma inserção no banco
for i in files_names:
    print(i)
    df_tmp = pd.read_csv( os.path.join( DATA_DIR, i ) )
    table_name = "tb_" + i.strip(".csv").replace("olist_", "").replace("_dataset", "")
    df_tmp.to_sql( table_name, 
                  connection,
                  if_exists='replace',
                  index=False )
