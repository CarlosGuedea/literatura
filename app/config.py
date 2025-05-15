import os
import urllib
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-insegura')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DRIVER = os.environ.get('DB_DRIVER')
    SERVER = os.environ.get('DB_SERVER')
    DATABASE = os.environ.get('DB_NAME')
    USERNAME = os.environ.get('DB_USER')
    PASSWORD = os.environ.get('DB_PASS')

    params = urllib.parse.quote_plus(
        f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
    )

    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
