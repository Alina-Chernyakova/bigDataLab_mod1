import pandas as pd 
from sqlalchemy import create_engine 

DB_URL = "postgresql://admin:admin123@localhost:5432/postgre"

def load_files(file_path: str, table_name: str, engine, chunksize: int = None):
    new_table_name=f"bronze_{table_name}"
    try:
        db=pd.read_csv(file_path)
        db.to_sql(name=new_table_name, con=engine, schema="bronze", if_exists="append",index=False, chunksize=chunksize)

    except FileNotFoundError as fr:
        raise FileNotFoundError(f"File not founded: {fr}")
    except Exception as e:
        raise RuntimeError(f"Something wrong: {e}")
    
try:
    engine = create_engine(DB_URL)

    tables=[('countries.csv', 'countries'),
            ('cities.csv', 'cities'),
            ('categories.csv', 'categories'),
            ('products.csv', 'products'),
            ('shops.csv', 'shops'),
            ('employees.csv', 'employees'),
            ('customers.csv', 'customers')]
    for file, name in tables:
        load_files(file, name, engine)
    load_files('sales.csv','sales',engine, chunksize=5000)
except Exception as e:
    raise RuntimeError(f"Someting wrong with pipeline: {e}")