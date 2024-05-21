class Event:
    def __init__(self, event_type, amount, origin=None, destination=None):
        self.event_type = event_type
        self.amount = amount
        self.origin = origin
        self.destination = destination