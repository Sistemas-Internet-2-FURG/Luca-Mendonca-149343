class Dealer:

    def __init__(self, id:int, name:str, address:str, contact:str):
        self.id = id
        self.name = name
        self.address = address
        self.contact = contact
    
    def json_me(self):
        return {"id": self.id, "name": self.name, "address": self.address, "contact": self.contact}