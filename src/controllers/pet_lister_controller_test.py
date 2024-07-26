from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController


class MockRepository:
    def __init__(self, first_name, last_name, pet_name, pet_type) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type


class MockPetsRepository:
    def list_pets(self):
        return[
            PetsTable(name="Fluffy", type="cat", id=4),
            PetsTable(name="Buddy", type="dog", id=47)
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Fluffy", "type": "cat"},
                {"name": "Buddy", "type": "dog"},
            ]
        }
    }

    assert response == expected_response
