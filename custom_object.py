from json import dump

class Facebook_Post:
    def __init__(self, message, created_time, picture):
        self.message = message
        self.created_time = created_time
        self.picture = picture
    
    def __str__(self):
        return dump(self)