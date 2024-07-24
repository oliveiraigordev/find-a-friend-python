from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable


class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_people(self) -> List:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PeopleTable).all()
                return pets
            except NoResultFound:
                return []
