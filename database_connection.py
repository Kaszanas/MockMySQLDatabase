import sqlalchemy

def create_engine(connection_string, database_name, drop_database = False):
    engine = sqlalchemy.create_engine(connection_string, echo=False)
    if drop_database:
        engine.execute(f"DROP DATABASE {database_name};")
    engine.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
    engine.execute(f"USE {database_name};")

    return engine
