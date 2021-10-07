# script python para integração de mysql => pivot select => python(pandas) => csv

import mysql.connector as sql
import random
import pandas as pd

db_connection = sql.connect(host='localhost', database='testpivot',
                            user='root', password='DigitalSchool1$')

tb = random.choice(pd.read_sql("SELECT * from maquina",
                               con=db_connection)["servidor"])
print(tb)

df = pd.read_sql(f"SELECT * FROM v_analytics WHERE servidor = '{tb}'",
                 con=db_connection)
print(df)
df.to_csv("Analytics.csv", index=False)
