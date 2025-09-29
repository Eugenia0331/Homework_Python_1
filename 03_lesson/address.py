class Address:
    def __init__(self, index: str, city: str, street: str, house: str, apartment: str):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"{self.index}, {self.city}, ул. {self.street}, д. {self.house}, кв. {self.apartment}"