import psycopg2 as pg
import json

class DatabaseConnections:
  def __init__(self):
    self.databases = json.load(open("databases.json"))
    self.connections = {}

  def set_up_connections(self):
    pass

db_cons = DatabaseConnections()