import psycopg2 as pg
import json

class DatabaseConnections:
  def __init__(self):
    self.databases = json.load(open("two_databases.json"))
    self.connections = {}
    self.username = "seta"
    self.password = "defaultUnsafePassword"
    
# can make this faster by commenting out most of the json in the file.
  def set_up_connections(self):
    for cntry, host in self.databases.items():
      self.create_connection(country=cntry, host=host)

  def create_connection(self, **kwargs):
    self.connections[kwargs["country"]] = pg.connect(
        host=kwargs["host"],
        database=kwargs["country"],
        user=self.username,
        password=self.password
      )