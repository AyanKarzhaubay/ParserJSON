class Address:
    def __init__(self, street: str, city: str, zipcode: str):
        self.street = street
        self.city = city
        self.zipcode = zipcode

    def __repr__(self):
        return f"Address(street='{self.street}', city='{self.city}', zipcode='{self.zipcode}')"

