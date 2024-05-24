import unittest

from flask import Flask, jsonify

from app.main import create_app


class TestBalanceEndpoints(unittest.TestCase):
    def setUp(self):
        # Configuração do ambiente de teste
        app = create_app()
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_reset_state(self):
        # Testa o endpoint para redefinir o estado do serviço
        response = self.client.post('/reset')
        self.assertEqual(response.status_code, 200)

    def test_get_balance_non_existing_account(self):
        # Testa o endpoint para obter saldo de uma conta inexistente
        response = self.client.get('/balance?account_id=1234')

        #se a conta não foi encontrada
        self.assertEqual(response.status_code, 404)

        self.assertEqual(response.data.decode('utf-8'), '0')

    def test_create_account_with_initial_balance(self):
        # Testa o endpoint para criar uma conta com saldo inicial
        response = self.client.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['destination']['balance'], 10)

    def test_deposit_into_existing_account(self):
        # Testa o endpoint para depositar em uma conta existente
        self.client.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        response = self.client.post('/event', json={"type": "deposit", "destination": "100", "amount": 20})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['destination']['balance'], 40)

    def test_get_balance_existing_account(self):
        # Testa o endpoint para obter saldo de uma conta existente
        self.client.post('/reset')
        self.client.post('/event', json={"type": "deposit", "destination": "100", "amount": 20})
        response = self.client.get('/balance?account_id=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.data.decode('utf-8')), 20)

    def test_withdraw_from_non_existing_account(self):
        # Testa o endpoint para sacar de uma conta inexistente
        response = self.client.post('/event', json={"type": "withdraw", "origin": "200", "amount": 10})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode('utf-8'), '0')

    def test_withdraw_from_existing_account(self):
        # Testa o endpoint para sacar de uma conta existente
        self.client.post('/event', json={"type": "deposit", "destination": "100", "amount": 20})
        response = self.client.post('/event', json={"type": "withdraw", "origin": "100", "amount": 5})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['origin']['balance'], 20)

    def test_transfer_from_existing_account(self):
        # Testa o endpoint para transferir de uma conta existente
        self.client.post('/event', json={"type": "deposit", "destination": "100", "amount": 20})
        response = self.client.post('/event', json={"type": "transfer", "origin": "100", "amount": 15, "destination": "300"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['origin']['balance'], 5)
        self.assertEqual(response.json['destination']['balance'], 15)

    def test_transfer_from_non_existing_account(self):
        # Testa o endpoint para transferir de uma conta inexistente
        response = self.client.post('/event', json={"type": "transfer", "origin": "200", "amount": 15, "destination": "300"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode('utf-8'), '0')

    def test_invalid_event(self):
        # Testa o endpoint para um evento inválido
        response = self.client.post('/event', json={"type": "invalid_event"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid input')

if __name__ == '__main__':
    unittest.main()

'''
NÃO PREVISTO

Manipulação com eventos negativos

if event.amount <= 0:  # Verifica se o valor da transferência é negativo ou zero
        return None  # Retorna None para indicar uma transferência inválida

Transferência com Saldo Insuficiente

'''