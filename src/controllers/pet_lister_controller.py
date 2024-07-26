from typing import Dict, List
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> PetsTable:
        pets = self.__pets_repository.list_pets()
        if not pets:
            raise Exception("Pets não encontrados!")
        return pets

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = [{"name": pet.name, "type": pet.type} for pet in pets]
        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }
