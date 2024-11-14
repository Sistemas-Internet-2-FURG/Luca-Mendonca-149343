class Sale():
    
    def __init__(self, id:int, client:str, dealer:str, car:str, price:int):
        self.id = id
        self.client = client
        self.dealer = dealer
        self.car = car
        self.price = price
    
    def json_me(self):
        return {"id": self.id, "client": self.client, "dealer": self.dealer, "car": self.car, "price": self.price}