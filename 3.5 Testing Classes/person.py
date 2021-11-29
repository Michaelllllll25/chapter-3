from datetime import datetime

class Person:
    def __init__(self, first_name: str, last_name: str, birth_year: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
    
    def get_age(self) -> int:
        """Get the person's age."""
        now = datetime.now()
        current_year = now.year
        return current_year - self.birth_year
    
    def get_last_first_format(self) -> str:
        """Get a formatted version of their name.
        
        Returns:
            A string in the format "last, first".
        """
        return f"{self.last_name} {self.first_name}"
