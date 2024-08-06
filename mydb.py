import psycopg2
import environ
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

env = environ.Env()
environ.Env.read_env()

database = psycopg2.connect(dbname='postgres',
      user=env("DB_USER"), host=env("DB_HOST"),
      password=env("DB_PASSWORD"))

database.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = database.cursor()

# Use the psycopg2.sql module instead of string concatenation 
# in order to avoid sql injection attacks.
cursor.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(env("DB_NAME")))
    )

print("All Done Db!")