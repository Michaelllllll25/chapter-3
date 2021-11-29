from person import Person

def test_person_attributes():
    p = Person("Dave", "Smith", 1988)
    assert p.first_name == "Dave"
    assert p.last_name == "Smith"
    assert p.birth_year == 1988

# test methods
def test_get_age():
    p = Person("Dave", "Smith", 2021)
    assert p.get_age() == 0

    p = Person("", "", 2020)
    assert p.get_age() == 1

def test_get_last_first():
    p = Person("Dave", "Smith", 0)
    assert p.get_last_first_format() == "Smith Dave"
