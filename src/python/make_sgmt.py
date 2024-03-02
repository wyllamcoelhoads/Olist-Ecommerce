import os
import sqlalchemy
import argparse
import pandas as pd

#Os endereços do projeto e de sub pastas
BASE_DIR = os.path.dirname( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ))
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SQL_DIR = os.path.join (BASE_DIR, 'src', 'sql' )

date = '2018-06-01'

with open( os.path.join( SQL_DIR, 'segmentos.sql' ) ) as query_file:
    query = query_file.read()

# Abrindo conexão com banco...
str_connection = 'sqlite:///{path}'
str_connection = str_connection.format( path = os.path.join( DATA_DIR, 'olist.db') )
connection = sqlalchemy.create_engine( str_connection )

create_query = f'''
CREATE TABLE tb_seller_sgmt AS 
{query}
;'''

insert_query = f'''
DELETE FROM tb_seller_sgmt WHERE dt_sgmt = '{date}';
INSERT INTO tb_seller_sgmt SELECT
{query}
;'''

connection.execute( create_query )
