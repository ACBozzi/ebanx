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
            if event.origin not in self.accounts:
                return None
            if self.accounts[event.origin] < event.amount:
                return None
            if event.destination not in self.accounts:
                self.accounts[event.destination] = 0
            self.accounts[event.origin] -= event.amount
            self.accounts[event.destination] += event.amount
            return {
                "origin": {"id": event.origin, "balance": self.accounts[event.origin]},
                "destination": {"id": event.destination, "balance": self.accounts[event.destination]}
            }
        return None

    # Método para resetar o estado do serviço
    def reset(self):
        self.accounts = {}
