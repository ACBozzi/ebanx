from . import TestEndpoints


class TestBalanceEndpoints(TestEndpoints):
    def test_reset_state(self):
        response = self.client.post('/reset')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'OK')

    def test_get_balance_non_existing_account(self):
        response = self.client.get('/balance?account_id=1234')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode('utf-8'), '0')

    def test_create_account_with_initial_balance(self):
        response = self.client.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['destination']['id'], '100')
        self.assertEqual(response.json()['destination']['balance'], 10)

    def test_deposit_into_existing_account(self):
        response = self.client.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['destination']['id'], '100')
        self.assertEqual(response.json()['destination']['balance'], 20)

    def test_get_balance_existing_account(self):
        response = self.client.get('/balance?account_id=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '20')

    def test_withdraw_from_non_existing_account(self):
        response = self.client.post('/event', json={"type": "withdraw", "origin": "200", "amount": 10})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode('utf-8'), '0')

    def test_withdraw_from_existing_account(self):
        response = self.client.post('/event', json={"type": "withdraw", "origin": "100", "amount": 5})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['origin']['id'], '100')
        self.assertEqual(response.json()['origin']['balance'], 15)

    def test_transfer_from_existing_account(self):
        response = self.client.post('/event', json={"type": "transfer", "origin": "100", "amount": 15, "destination": "300"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['origin']['id'], '100')
        self.assertEqual(response.json()['origin']['balance'], 0)
        self.assertEqual(response.json()['destination']['id'], '300')
        self.assertEqual(response.json()['destination']['balance'], 15)

    def test_transfer_from_non_existing_account(self):
        response = self.client.post('/event', json={"type": "transfer", "origin": "200", "amount": 15, "destination": "300"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode('utf-8'), '0')


if __name__ == '__main__':
    unittest.main()