class Car:

    def __init__(self, id:int, name:str, price:int):
        self.id = id
        self.name = name
        self.price = price
    
    def json_me(self):
        return {"id": self.id, "name": self.name, "price": self.price}