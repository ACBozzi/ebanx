#Camada de Lógica de Negócios

class BalanceService:

    #Construtor da classe BalanceService
    def __init__(self):
        self.accounts = {}

    # Método para obter o saldo de uma conta específica
    def get_balance(self, account_id):
        return self.accounts.get(account_id)

    # Método para processar eventos que alteram o saldo
    def process_event(self, event):
        if event.event_type == 'deposit':
            if event.destination not in self.accounts:
                self.accounts[event.destination] = 0
            self.accounts[event.destination] += event.amount
            return {"destination": {"id": event.destination, "balance": self.accounts[event.destination]}}

        elif event.event_type == 'withdraw':
            if event.origin not in self.accounts:
                return None
            if self.accounts[event.origin] < event.amount:
                return None
            self.accounts[event.origin] -= event.amount
            return {"origin": {"id": event.origin, "balance": self.accounts[event.origin]}}

        elif event.event_type == 'transfer':
            #verifica se a conta de origem existe
            if event.origin not in self.accounts:
                return None
            
            #verifica se o saldo de origem é suficiente
            if self.accounts[event.origin] < event.amount:
                return None
            
            #verifica se a conta de destino existe
            if event.destination not in self.accounts:
                self.accounts[event.destination] = 0

            self.accounts[event.origin] -= event.amount #tira da origem
            self.accounts[event.destination] += event.amount #soma no destino

            return {
                "origin": {"id": event.origin, "balance": self.accounts[event.origin]},
                "destination": {"id": event.destination, "balance": self.accounts[event.destination]}
            }
        return None

'''
class EventFactory
@staticmethod
    def create_event(event_type, amount, destination=None, origin=None):
        if event_type == 'deposit':
            return DepositEvent(amount, destination)
        elif event_type == 'withdraw':
            return WithdrawEvent(amount, origin)
        elif event_type == 'transfer':
            return TransferEvent(amount, origin, destination)
        else:
            raise ValueError("Invalid event type")

class DepositEvent:
    def __init__(self, amount, destination):
        self.event_type = 'deposit'
        self.amount = amount
        self.destination = destination
'''
    # Método para resetar o estado do serviço
def reset(self):
    self.accounts = {}
