from peewee import *


database=MySQLDatabase(
    "inventario-reparaciones",
    user="root", 
    password="",
    host="localhost",
    port=3306
)
