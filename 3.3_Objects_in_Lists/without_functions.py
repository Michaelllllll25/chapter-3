"""
3.3 Lesson: objects in lists
Looping and accessing fields 
Simple search
- Break it down from list of marks
- Filtering
Object pointers vs primitive data types
"""
#clases- 1nd
#functions- 2nd
#globa code- last
class Waterbottle:
    def __init__(self, brand: str, volume: int, colour: str) -> None:
        self.brand = brand                                                 # name doesnt matter, can equal anything
        self.volume = volume
        self.colour = colour

#wb = Waterbottle("Contigo", 750, "blue")
#wb2 = Waterbottle("Evian", 350, "transparent")

# bottles = [wb, wb2]
bottles = [
    Waterbottle("Contigo", 750, "blue"),
    Waterbottle("Evian", 350, "transparent"),
    Waterbottle("Figi", 400, "clear"),
    Waterbottle("Desani", 200, "black")
]

# print(bottles)

# find first transparent waterbottle
# -> set up loop
found = None
for bottle in bottles:
    if bottle.colour == "transparent":
        # print(bottle0
        found = bottle
        break

print(f"Found: {found}")

# filter only bottles >= 350 ml
filtered = []
for bottle in bottles:
    if bottle.volume >= 350:
        filtered.append(bottle)

print(len(filtered))
        
for bottle in filtered:
    print(bottle.volume)
    
########################################### with functions
def find_bottle_by_colour():
    found = None
    for bottle in bottles:
        if bottle.colour == "transparent":
            # print(bottle0
            found = bottle
            break

    print(f"Found: {found}")




filtered = []
for bottle in bottles:
    if bottle.volume >= 350:
        filtered.append(bottle)

print(len(filtered))
        
for bottle in filtered:
    print(bottle.volume)


