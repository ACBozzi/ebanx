import unittest

from app import create_app


class TestBalanceEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.client = app.test_client()

    def test_reset_state(self):
        response = self.client.post('/reset')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
