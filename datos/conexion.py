from decouple import config
from peewee import MySQLDatabase

def conectar_db():
   database = MySQLDatabase(config('db'), **{
      