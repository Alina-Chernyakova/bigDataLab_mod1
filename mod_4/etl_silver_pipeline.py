import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://admin:admin123@localhost:5432/postgre"
BOOL_VALUES = {"yes": True, "no": False}
engine = create_engine(DB_URL)


def validate_and_fix_date(data_frame: pd.DataFrame, column: str) -> pd.DataFrame:
    if column in data_frame.columns:
        data_frame[column] = pd.to_datetime(data_frame[column], errors="coerce")
        data_frame[column] = data_frame[column].fillna(pd.Timestamp("1900-01-01"))
    return data_frame


def fix_bool(data_frame: pd.DataFrame, column: str) -> pd.DataFrame:
    if column in data_frame.columns:
        data_frame[column] = (
            data_frame[column].astype(str).str.strip().str.lower().map(BOOL_VALUES)
        )
        data_frame[column] = data_frame[column].fillna(False).astype(bool)
    return data_frame


def fill_silver_layer():

    for table in [
        "countries",
        "cities",
        "categories",
        "products",
        "shops",
        "customers",
    ]:
        data_frame = pd.read_sql_table(
            table_name=f"bronze_{table}", con=engine, schema="bronze"
        )
        data_frame = fix_bool(data_frame, "resistant")
        data_frame = fix_bool(data_frame, "is_allergic")
        data_frame.to_sql(
            name=f"bronze_{table}",
            con=engine,
            schema="silver",
            if_exists="append",
            index=False,
        )

        if table == "products":
            data_frame = validate_and_fix_date(data_frame, "modify_timestamp")

        data_frame.to_sql(
            name=f"bronze_{table}",
            con=engine,
            schema="silver",
            if_exists="append",
            index=False,
        )

    df_employees = pd.read_sql_table(
        table_name="bronze_employees", con=engine, schema="bronze"
    )
    df_employees = validate_and_fix_date(df_employees, "birth_date")
    df_employees = validate_and_fix_date(df_employees, "hire_date")
    df_employees.to_sql(
        name="silver_employees",
        con=engine,
        schema="silver",
        if_exists="append",
        index=False,
    )

    chunks = pd.read_sql_table(
        table_name="bronze_sales", con=engine, schema="bronze", chunksize=10000
    )

    for chunk in chunks:
        chunk = chunk.dropna(subset=["sales_timestamp"])
        chunk["sales_timestamp"] = pd.to_datetime(
            chunk["sales_timestamp"], errors="coerce"
        )
        chunk = chunk.dropna(subset=["sales_timestamp"])

        if "city_id" not in chunk.columns:
            chunk["city_id"] = None

        if "shop_id" not in chunk.columns:
            chunk["shop_id"] = None

        chunk.to_sql(
            name="silver_sales",
            con=engine,
            schema="silver",
            if_exists="append",
            index=False,
        )


fill_silver_layer()
