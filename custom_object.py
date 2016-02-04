from json import encode

class Facebook_Post:
    def __init__(self, message, created_time, picture):
        self.message = message
        self.created_time = created_time
        self.picture = picture
    
    def __str__(self):
        return encode(self)