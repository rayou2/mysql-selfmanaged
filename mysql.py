#sudo apt-get install python3-dev default-libmysqlclient-dev
#pip install pymysql

from sqlalchemy import create_engine
import pandas as pd

MYSQL_HOSTNAME = '35.193.34.22' # you probably don't need to change this
MYSQL_USER = 'ramon'
MYSQL_PASSWORD = 'ahi2022'
MYSQL_DATABASE = 'db1'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string

db = create_engine(connection_string)

query = 'select * from db1.table1;'

df = pd.read_sql(query, con=db)

dummy_df = pd.read_csv('https://raw.githubusercontent.com/rayou2/HHA-507-2022/main/descriptive/example1/data/Altair.csv')
dummy_df.to_sql('dummydata_table', con=db, if_exists='replace')

sql_query = """select * from dummydata_table where grade = '4' """

results = pd.read_sql(sql_query, con=db)
results