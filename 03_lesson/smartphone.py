class Smartphone:
    def __init__(self, brand: str, model: str, phone_number: str):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.brand} {self.model} ({self.phone_number})"