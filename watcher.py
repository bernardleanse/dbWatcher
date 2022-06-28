from boot import db_cons

class Watcher:
  def __init__(self):
    self.response_record_counts = self.generate_quantities()

  def generate_quantities(self):
    dictionary = {}
    for country_code, connection in db_cons.connections.items():
      dictionary[country_code] = self.get_quantity_of_records(connection)
    return dictionary

  def watch(self):
    for country_code, connection in db_cons.connections.items():
      number_of_records = self.get_quantity_of_records(connection)
      if self.response_record_counts[country_code] != number_of_records:
        print("new data detected")
        self.pull_in_new_data()
        self.response_record_counts[country_code] = number_of_records

  def get_quantity_of_records(self, connection):
    cursor = connection.cursor()
    cursor.execute("select count (*) from responses;")
    quant = cursor.fetchone()[0]
    cursor.close()
    return quant


  def pull_in_new_data(self):
    pass

