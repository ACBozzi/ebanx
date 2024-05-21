#lógica de negócios

class BalanceService:
    def __init__(self):

        #inicializa com saldo 0
        self.balance = 0

    def get_balance(self):
        
        #retorna o saldo atual
        return self.balance

    def process_event(self, event):

        #processo um evento e atualiza
        if event.event_type == 'credit':
            self.balance += event.amount
        elif event.event_type == 'debit':
            self.balance -= event.amount