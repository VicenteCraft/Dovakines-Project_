from peewee import *
from decouple import config

database = MySQLDatabase(config('db'), **{
    'charset': 'utf8mb4',
    'host': config('host'), 
    'port': config('port'), 
    'user': config('user'), 
    'password': config('password')})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database
