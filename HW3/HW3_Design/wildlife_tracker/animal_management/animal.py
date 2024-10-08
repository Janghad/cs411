from typing import Any, Optional, Dict

class Animal:
    def __init__(self, 
        animal_id: int,
        species: str,
        health_status: Optional[str] = None,
        age: Optional[int] = None):
        self.animal_id = animal_id
        self.health_status = health_status
        self.species = species
        self.age = age

    def get_animal_details(self) -> dict[str, Any]:
        pass
    
    def update_animal_details(self, **kwargs: Dict[str, Any]) -> None:
        pass
