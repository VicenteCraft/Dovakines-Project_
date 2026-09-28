from peewee import *
from decouple import config

database = MySQLDatabase(config('db'), **{
    'charset': 'utf8mb4',
    'host'
}
