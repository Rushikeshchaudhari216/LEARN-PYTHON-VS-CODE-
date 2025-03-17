from typing import List, Tuple, Dict, Union

# Example of a List
numbers: List[int] = [1, 2, 3, 4, 5]
print(numbers)

# Example of a Tuple
coordinates: Tuple[int, str] = (10, "Men Are Brave")
print(coordinates)

# Example of a Dict
person_age: Dict[str, int] = {"Rushi": 22, "Gayatri": 23}
print(person_age)

# Example of a Union
def get_id(value: Union[int, str]) -> str:
    return f"ID: {value}"
print(get_id(123))
print(get_id("ABC"))
