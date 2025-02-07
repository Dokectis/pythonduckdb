import duckdb

# directly query a Pandas DataFrame
import pandas as pd
pandas_df = pd.DataFrame({"Column_name": [74]})
duckdb.sql("SELECT * FROM pandas_df").show()




# directly query a Polars DataFrame
# import polars as pl
# polars_df = pl.DataFrame({"a": [42]})
# duckdb.sql("SELECT * FROM polars_df").show()


# directly query a pyarrow table
# import pyarrow as pa
# arrow_table = pa.Table.from_pydict({"a": [42]})
# duckdb.sql("SELECT * FROM arrow_table")