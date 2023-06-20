import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')

user = os.getenv('user')
db_name = os.getenv('database')
port = os.getenv('port')
password = os.getenv('password')
host = os.getenv('host')