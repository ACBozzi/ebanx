#modelo para os eventos

class Event:
    def __init__(self, event_type, amount):
        
        #representador do modelo
        self.event_type = event_type
        self.amount = amount