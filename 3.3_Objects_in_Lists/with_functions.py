"""
3.3 Lesson: objects in lists with functions
"""

from typing import List

class Waterbottle:
    def __init__(self, brand: str, volume: int, colour: str) -> None:
        self.brand = brand                                                 # name doesnt matter, can equal anything
        self.volume = volume
        self.colour = colour
    
    def __str__(self) -> str:
        return f"A {self.colour} {self.brand} bottle, {self.volume}"

    def find_bottle_by_colour(bottles: list[Waterbottle], 
                              colour: str) -> Waterbottle:
        for bottle in bottles:
            if bottle.colour == "transparent":
                return bottle

    def filter_by_min_volume(bottles: List[Waterbottle], min_volume: int) -> List[Waterbottle]:
        filtered = []
        for bottle in bottles:
            if bottle.volume >= min_volume:
                filtered.append(bottle)

        return filtered

bottles = [
    Waterbottle("Contigo", 750, "blue"),
    Waterbottle("Evian", 350, "transparent"),
    Waterbottle("Figi", 400, "clear"),
    Waterbottle("Desani", 200, "black")
]


found = find_bottle_by_colour(bottles, "transparent")
print(f"Found: {found.brand}")


result = filter_by_min_volume(bottles, 350)
print(*result, sep="\n")
