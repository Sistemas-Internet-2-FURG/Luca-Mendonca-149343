class Client():

    def __init__(self, id:int, name:str, email:str, phone:str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
    
    def json_me(self):
        return {"id": self.id, "name": self.name, "email": self.email, "phone": self.phone}