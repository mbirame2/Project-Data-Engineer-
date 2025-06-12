import sqlite3

def load_to_sqlite(kpis, db_path=':memory:'):
    conn = sqlite3.connect(db_path)
    for kpi_name, kpi_df in kpis.items():
        kpi_df = kpi_df.reset_index()
        kpi_df.columns = ['team', 'value']
        kpi_df.to_sql(kpi_name, conn, if_exists='replace', index=False)
    return conn
