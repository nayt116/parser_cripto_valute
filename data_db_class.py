from dataclasses import dataclass

@dataclass
class data_DB:
    name_db_table_users:str

class add_to_data:
    def __init__(self, name):
        self.name = data_DB(name)