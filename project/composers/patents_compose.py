from project.composers.compose import Compose
from datetime import datetime

class PatentsCompose(Compose):

    def __init__(self, database_cache_repository):
        self.repository = database_cache_repository

    def insert_consult(self):
        return self.repository.insert(values={"dateregister": str(datetime.today())},
                                      entity_name="registers")
