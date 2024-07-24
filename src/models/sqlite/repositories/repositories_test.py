from src.models.sqlite.settings.connection import db_connection_hander
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository


db_connection_hander.connect_to_db()

def test_list_pets():
    repo = PetsRepository(db_connection_hander)
    response = repo.list_pets()
    print(response)

def test_list_people():
    repo = PeopleRepository(db_connection_hander)
    response = repo.list_people()
    print(response)
